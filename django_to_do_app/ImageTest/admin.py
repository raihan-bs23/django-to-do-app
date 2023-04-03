from django.contrib import admin

# Register your models here.
from . import models


class ImageGet(admin.ModelAdmin):
    list_display = (
        'title',
        'image_tag',
    )


admin.site.register(models.ImageShow, ImageGet)
