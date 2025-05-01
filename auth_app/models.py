from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    enrollment_date = models.DateField(auto_now_add=True)

class InstructorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='instructor_profile')
