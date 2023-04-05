from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from base.models import User, Submission


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["name", "email", "password1", "password2", ]

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ["email","name","bio","avatar"]

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update({'class': 'input'})
        self.fields["name"].widget.attrs.update({'class': 'input'})
        self.fields["bio"].widget.attrs.update({'class': 'text-area'})
        self.fields["avatar"].widget.attrs.update({'class': 'input'})


class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(SubmissionForm, self).__init__(*args, **kwargs)

        self.fields["event"].widget.attrs.update({'class': 'input'})
        self.fields["participant"].widget.attrs.update({'class': 'input-disabled'})
        self.fields["details"].widget.attrs.update({'class': 'text-area'})
