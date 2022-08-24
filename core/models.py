from django.db import models
from django.contrib import admin

class Post(models.Model):
    text = models.TextField(max_length=300)
    photo = models.ImageField(upload_to='uploads/%d-%m-%y/')
    published = models.BooleanField(default=False)
    date = models.DateField(auto_now=False,auto_now_add=False,auto_created=False)
    hours = models.TimeField(auto_created=False, auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.date.strftime('%d/%m/%y')
