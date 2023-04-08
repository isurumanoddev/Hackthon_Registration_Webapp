from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    avatar =models.ImageField(default="avatar.png")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


    def imageURL(self):
        try:
            url = self.avatar.url
        except:
            url = ""

        return url


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, blank=True)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(default="Hackathon-Logo.png")

    def __str__(self):

        return self.name

    def imageURL(self):
        try:
            url = self.poster.url
        except:
            url = ""

        return url


class Submission(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name="submission")
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    details = models.TextField(null=True, blank=True)
    submitted_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event) + " ----- " + str(self.participant)
