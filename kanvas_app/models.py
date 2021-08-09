from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField, IntegerField
from django.db.models.deletion import CASCADE
from django.db.models.fields import NullBooleanField
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField

class Course(models.Model):
    name = CharField(max_length=255, unique=True)

    users = ManyToManyField(User, related_name="courses")

    def __str__(self):
        return self.name

class Activities(models.Model):
    title = CharField(max_length=255, unique=True)
    points = IntegerField()

    def __str__(self):
        return self.title

class Submissions(models.Model):
    grade = IntegerField(null=True)
    repo = CharField(max_length=255)

    user_id = ForeignKey(User, on_delete=CASCADE, related_name="submission_id")
    activity_id = ForeignKey("Activities", on_delete=CASCADE, related_name="submissions")

    def __str__(self):
        return self.repo
