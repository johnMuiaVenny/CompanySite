from django.db import models

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
