from django.db import models


# Create your models here.
class ImageShow(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    class Meta:
        db_table = 'demo_image'
