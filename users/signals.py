# to auto create profile (img) for each user
# why we use signals ? cause a problem happens when we use MODELS in this process
# post_save is fired after object is saved

from django.db.models.signals import post_save

# the sender of the signal
from django.contrib.auth.models import User

# the receiver of the signal
from django.dispatch import receiver
# import profile
from .models import Profile

# user send a signal by saving(register) and @receiver decorate receive this and send this
# params "sender,instance,created, **kwargs" to our function to create a profile
@receiver(post_save, sender=User)
def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender,instance, **kwargs):
    instance.profile.save()