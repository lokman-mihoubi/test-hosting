from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)
class Car(models.Model):
    name= models.CharField(max_length=50)
    price=models.IntegerField(default=1)
    image = models.ImageField(upload_to=image_upload)
    SLug = models.SlugField(blank=True, null=True )

    def save(self , *args , **kwargs):
        if not self.SLug :
            self.SLug = slugify(self.name)
        super(Car, self).save(*args , **kwargs)
    def get_absolute_url(self):
        return reverse('home:car_detail', kwargs={'slug': self.SLug})
