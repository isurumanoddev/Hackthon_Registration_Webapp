from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    # avatar =models.ImageField(null=True,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, blank=True)
    date = models.DateTimeField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Submission(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name="submission")
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    details = models.TextField(null=True, blank=True)
    submitted_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event) + " ----- " + str(self.participant)
