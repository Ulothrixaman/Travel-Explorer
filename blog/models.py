from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User


# Create your models here.


# Account Model
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(upload_to='users/', null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    



# Gallery Model
class Gallery(models.Model):
    img_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='gallery/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def gal_img(self):
        return format_html(
            '<img src="/media/{}" style="height: 50px; width: 50px"/>'.format(self.image)
        )

    def __str__(self):
        return str(self.img_id)


# Packages Model
class Packages(models.Model):
    pack_id = models.AutoField(primary_key=True)
    pack_img = models.ImageField(upload_to='packages/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=20)
    url = models.CharField(max_length=50)
    add_date = models.DateTimeField(auto_now_add=True, null=False)

    def pac_img(self):
        return format_html(
            '<img src="/media/{}" style="height: 50px; width: 50px"/>'.format(self.pack_img)
        )

    def __str__(self):
        return str(self.title)

    def str(self):
        return str(self.description)


class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    url = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)


# Trips Model
class Trips(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    trip_id = models.AutoField(primary_key=True)
    destination = models.CharField(max_length=100)
    departure = models.DateTimeField(null=True)
    arrival = models.DateTimeField(null=True)
    review = models.TextField()

