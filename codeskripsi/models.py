# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Class(models.Model):
    class_name = models.CharField(max_length=255)

    def __str__(self):
        return self.class_name

class Presence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status_choices = [
        ('present', 'Present'),
        ('absent', 'Absent'),
    ]
    status = models.CharField(max_length=10, choices=status_choices)
    schedule = models.DateTimeField(null=True, blank=True)
    schedule_limit = models.DateTimeField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.status} - {self.timestamp}"
