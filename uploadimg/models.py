from django.db import models
from .utils import image_editor
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images')
    
    # We Will use this later if we want databas interaction------------------------------------------
    # def save(self,image_front, color, position, image_back, *args, **kwargs):
    #     x = image_editor(image_front, color, position, image_back)
    #     buffer = BytesIO()
    #     x.save(buffer, format='png')
    #     image_png = buffer.getvalue()

    #     self.image.save(str(self.image), ContentFile(image_png), save=False)
    #     super().save(*args, **kwargs)

    class Meta:
        db_table = "myapp_image"