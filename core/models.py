from django.db import models

def photo_upload(instance, filename):
    return f'uploads/{instance.date.strftime("%d-%m-%y")}/{filename}'

class Post(models.Model):
    text = models.TextField(max_length=300)
    photo = models.ImageField(upload_to=photo_upload)
    date = models.DateField(auto_now=False,auto_now_add=False,auto_created=False)
    hours = models.TimeField(auto_created=False, auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.date.strftime('%d/%m/%y')

 


class Linkedin_Account(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.email