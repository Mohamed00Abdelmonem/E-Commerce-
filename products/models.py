# from django.db import models
#
#
#
# # Create your models here.
#
#
# class Section(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#
#     def __str__(self):
#         return self.name
#
#
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     price = models.IntegerField()
#     photo = models.ImageField(upload_to='product/photos/')
#     video = models.FileField(upload_to='product/video/')
#     section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         return self.name
#
#
#
#
#
#
#
#
#

from django.db import models



# Create your models here.


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='product/photos/')
    video = models.FileField(upload_to='product/video/')
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name









