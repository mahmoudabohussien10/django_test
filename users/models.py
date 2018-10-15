from django.db import models
from django.contrib.auth.models import User
# import image pillow
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return '{} Profile'.format(self.user.username)

    def save(self):
        # call super save profile to auto save model data (img)
        super().save()
        # resize our image
        img = Image.open(self.image.path)
        # check our image width and height
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # resize
            img.thumbnail(output_size)
            # overwrite our uploaded image
            img.save(self.image.path)
