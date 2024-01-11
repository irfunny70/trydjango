from django.db import models
from django.utils.text import slugify
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True,null=True)
    content = models.TextField()
    #last created
    timestamp = models.DateTimeField(auto_now_add=True)
    #when it was last updated
    updated = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)