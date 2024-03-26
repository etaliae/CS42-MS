from django.db import models

class User(models.Model):
    email = models.EmailField(primary_key=True, unique=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
