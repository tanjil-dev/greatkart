from django.db import models

class Images(models.Model):
    image_1 = models.ImageField(upload_to='photos/products')
    image_2 = models.ImageField(upload_to='photos/products')
    image_3 = models.ImageField(upload_to='photos/products')
    image_4 = models.ImageField(upload_to='photos/products')
    
    crousel_image_1 = models.ImageField(upload_to='photos/crousel')
    crousel_image_2 = models.ImageField(upload_to='photos/crousel')
    crousel_image_3 = models.ImageField(upload_to='photos/crousel')
    
    image_bottom_1 = models.ImageField(upload_to='photos/products')
    image_bottom_2 = models.ImageField(upload_to='photos/products')
    image_bottom_3 = models.ImageField(upload_to='photos/products')
    image_bottom_4 = models.ImageField(upload_to='photos/products')
    