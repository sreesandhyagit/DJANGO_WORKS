from django.db import models
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=70)
    place=models.CharField(max_length=30)
    about=models.TextField()
    image=models.ImageField(upload_to="author")
    dob=models.DateField()
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    def save(self):
        if not self.slug:
            self.slug=slugify(self.name)
        return super().save()
