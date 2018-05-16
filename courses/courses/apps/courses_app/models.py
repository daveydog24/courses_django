from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
    def validate_user(self, postData):
        errors = {}

        if len(postData['name']) < 5:
            errors['name'] = "Course Name can not be less than 5 characters."

        if len(postData['description']) < 15:
            errors['description'] = "Description cant be less than 15 characters."

        return errors

class Courses(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# class Description(models.Model):
#     description = models.ForeignKey(Courses, related_name="teams")

