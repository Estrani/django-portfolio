from django.db import models

class JourneyBanner(models.Model):
    h2 = models.fields.CharField(max_length=50)
    skills = models.fields.TextField()
    orga_img = models.ImageField()
    orga_link = models.URLField()

    def __str__(self):
        return f'{self.h2}'
