from django.db import models


# Create your models here.
class imageProcess(models.Model):
    image_upload = models.ImageField(upload_to='images/')

    class Meta:
        db_table = "myapp_image"
