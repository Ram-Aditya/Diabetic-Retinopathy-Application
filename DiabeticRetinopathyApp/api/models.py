from django.db import models


# Create your models here.


class ImageUpload(models.Model):
    name = models.CharField(max_length=50)
    Main_Img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
