from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Profile

@receiver(pre_save,sender=Profile)
def before_saving_profile(sender,instance,**kwargs):
    if not instance.profile_pic:
        instance.profile_pic="profile/default_profile_image.jpg"
