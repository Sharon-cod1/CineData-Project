from django.db import models

from django.contrib.auth.models import AbstractUser

class Rolechoices(models.TextChoices):

    ADMIN = 'Admin', 'Admin'

    USER = 'User', 'User'



class Profile(AbstractUser):

    role = models.CharField(max_length=20,choices=Rolechoices.choices)

    mobile_num = models.CharField(max_length=10, unique=True)

    def __str__(self):

        return self.email
    
    class Meta:

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'



