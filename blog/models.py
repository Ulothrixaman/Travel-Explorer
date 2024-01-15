from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField


# Create your models here.

# Category model

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="height: 50px; width:50px; border-radius: 50%"/>'.format(self.image))

    def __str__(self):
        return self.title


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
    description = HTMLField()
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


# Post model
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = HTMLField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField('post/')

    def image_pot(self):
        return format_html(
            '<img src="/media/{}" style="width:50px; height:50px; border-radius:50%"/>'.format(self.image))

    def __str__(self):
        return self.title
