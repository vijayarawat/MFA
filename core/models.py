from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class UserDetails(models.Model):
    id = models.CharField(max_length=50, null = False,unique = True, primary_key=True)
    name= models.CharField(max_length=50, null = False)
    password = models.CharField(max_length=10, null = False)
    email = models.EmailField(max_length=254, null = False, unique=True)


    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
        
