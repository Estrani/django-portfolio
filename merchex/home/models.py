from django.db import models

class FirstPage(models.Model):
    h1 = models.fields.CharField(max_length=50)
    h2 = models.fields.CharField(max_length=50)
    introduction = models.fields.TextField()
    bg_img = models.ImageField()

