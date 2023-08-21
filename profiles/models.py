from django.db import models

# Create your models here.

class UserProfile(models.Model):
    users_image = models.FileField(upload_to="image")