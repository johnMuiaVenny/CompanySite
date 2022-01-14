from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
#from django.contrib.auth.models import AbstractUser

# Create your models here.


class DIRECTORS(models.Model):
    Name = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    Image = models.FileField(upload_to='Team')
    FB_Account = models.CharField(max_length=200, null=True, blank=True)
    Twitter_Account = models.CharField(max_length=200, null=True, blank=True)
    Instagram_Account = models.CharField(max_length=200, null=True, blank=True)
    LinkedIn_Account = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.Name


class CONTACT(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Subject = models.CharField(max_length=200)
    Message = models.TextField()

    def __str__(self):
        return self.Name


class PROJECT(models.Model):
    Name = models.CharField(max_length=200)
    Type = models.CharField(max_length=200, default='Web-App')
    Link = models.CharField(max_length=200, null=True, blank=True)
    Display_Image = models.FileField(upload_to='Projects')

    def __str__(self):
        return self.Name


class PROFILE(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    FName = models.CharField(max_length=200)
    LName = models.CharField(max_length=200)
    Email = models.EmailField(null=True, blank=True)
    Image = models.ImageField(upload_to='Profile')

    def __str__(self):
        return str(self.user)


class BLOG(models.Model):
    ABOUTS  = (
        ('WEB', 'WEB'),
        ('ADROID', 'ADROID'),
        ('DESKTOP', 'DESKTOP'),
        ('SYSTEMS', 'SYSTEMS'),
    )
    Title = models.CharField(max_length=200)
    Date_Created = models.DateTimeField(default=datetime.now)
    Image = models.ImageField(upload_to='Blogs')
    ABOUT = models.CharField(max_length=200, choices=ABOUTS, null=True, blank=True)
    Description = models.TextField()

    def __str__(self):
        return self.Title

