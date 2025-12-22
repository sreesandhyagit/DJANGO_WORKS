from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from django.dispatch import receiver
from manager.models import Author,Book
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
import os

@receiver(pre_save,sender=Author)
def before_saving_author(sender,instance,**kwargs):
    if not instance.image:
        instance.image="author/default_author_image.jpg"

@receiver(post_save,sender=Author)
def after_author_save(sender,instance,created,**kwargs):
    if created:
        print(f"New author named{instance.name} was created")
    else:
        print(f"Author {instance.name} details has been updated")

@receiver(pre_delete,sender=Author)
def before_author_delete(sender,instance,**kwargs):
    author=Author.objects.get(id=instance.id)
    print("CHECKING : ",Book.objects.filter(author=author).exists())
    if Book.objects.filter(author=author).exists():
        raise PermissionDenied
    else:
        print("Deleting.....")

@receiver(post_delete,sender=Author)
def after_author_delete(sender,instance,**kwargs):
    if instance.image and instance.image!="author/default_author_image.jpg":
        image_path=instance.image.path
        if os.path.exists(image_path):
            os.remove(image_path)
            print("Author image deleted from server")