from PIL import Image
from django.db import models
from django.contrib.auth.models import User
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='profile_pics',
        default='profile_pics/avatar_default.jpg'
    )

def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    if self.image.name == 'profile_pics/avatar_default.jpg':
        return

    if not os.path.isfile(self.image.path):
        return

    img = Image.open(self.image.path)


    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    width, height = img.size
    min_side = min(width, height)

    left = (width - min_side) / 2
    top = (height - min_side) / 2
    right = (width + min_side) / 2
    bottom = (height + min_side) / 2

    img = img.crop((left, top, right, bottom))
    img = img.resize((300, 300), Image.LANCZOS)

    img.save(self.image.path, format="JPEG", quality=90)
