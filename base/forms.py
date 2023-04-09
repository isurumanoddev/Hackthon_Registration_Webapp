from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from base.models import User, Submission


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", ]

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ["email","username","bio","avatar"]

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update({'class': 'form-control'})
        self.fields["username"].widget.attrs.update({'class': 'form-control'})
        self.fields["bio"].widget.attrs.update({'class': 'form-control-textarea'})
        self.fields["avatar"].widget.attrs.update({'class': 'form-control'})


class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(SubmissionForm, self).__init__(*args, **kwargs)

        self.fields["event"].widget.attrs.update({'class': 'form-control'})
        self.fields["participant"].widget.attrs.update({'class': 'form-control-disabled'})
        self.fields["details"].widget.attrs.update({'class': 'form-control'})
