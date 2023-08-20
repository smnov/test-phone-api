from django.db import models

class User(models.Model):
    phone_number = models.CharField(max_length=20)
    auth_code = models.CharField(max_length=4)
    invite_code = models.CharField(max_length=6, null=True)