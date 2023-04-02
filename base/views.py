from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from base.models import User, Event, Submission
from base.forms import CreateUserForm, SubmissionForm



def home(request):
    participants = User.objects.all()

    events = Event.objects.all()
    context = {"participants": participants, "events": events}
    return render(request, "home.html", context)


def user_register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("home")

    context = {"form": form}
    return render(request, "register.html", context)


def user_login(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    try:
        User.objects.get(email=email)
    except:
        print("user not exist")

    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect("home")

    else:
        print("Login Error")

    context = {}
    return render(request, "login.html", context)


def user_logout(request):
    logout(request)
    return redirect("home")


@login_required(login_url="login")
def event_page(request, pk):
    event = Event.objects.get(id=pk)
    participants = event.participants.all()

    user = request.user

    registered = user.event_set.filter(id=event.id).exists()
    submitted = Submission.objects.filter(participant=request.user, event=event).exists()

    context = {"event": event, "participants": participants, "registered": registered, "submitted": submitted}
    return render(request, "event_page.html", context)


@login_required(login_url="login")
def event_registration(request, pk):
    event = Event.objects.get(id=pk)
    participant = request.user

    if request.method == "POST":
        event.participants.add(participant)
        print(event.participants)

        return redirect("event-page", pk=event.id)

    context = {"event": event}
    return render(request, "event_registration.html", context)


@login_required(login_url="login")
def user_profile(request):
    user = request.user

    registered_events = user.event_set.all()

    submitted_events = user.submission.all()
    print("submitted_events ", submitted_events)

    context = {"user": user, "registered_events": registered_events, "submitted_events": submitted_events}
    return render(request, "user_profile.html", context)


@login_required(login_url="login")
def event_submission(request, pk):
    event = Event.objects.get(id=pk)
    form = SubmissionForm(initial={"event": event, "participant": request.user})
    if request.method == "POST":
        form = SubmissionForm(request.POST, initial={"event": event, "participant": request.user})
        if form.is_valid():
            form.save()
            return redirect("event-page", pk=event.id)
    context = {"form": form}
    return render(request, "submission_form.html", context)


@login_required(login_url="login")
def update_submission(request, pk):
    submission = Submission.objects.get(id=pk)
    form = SubmissionForm(instance=submission)
    if request.method == "POST":
        form = SubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect("user-profile")
    context = {"form": form}
    return render(request, "submission_form.html", context)
