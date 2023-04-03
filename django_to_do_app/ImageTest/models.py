from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class ImageShow(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.image.url))

    class Meta:
        db_table = 'demo_image'
