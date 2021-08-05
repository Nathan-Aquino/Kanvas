from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField
from django.db.models.fields.related import ManyToManyField

class Course(models.Model):
    name = CharField(max_length=255, unique=True)

    users = ManyToManyField(User, related_name="courses")

    def __str__(self):
        return self.name

