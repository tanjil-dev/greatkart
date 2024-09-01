from django.db import models

# Create your models here.

class Images_Home(models.Model):
    
    Imgaes_of_home = models.CharField(max_length=50,blank=True)
    
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
    
    card_1_1 = models.ImageField(upload_to='photos/crousel')
    card_1_2 = models.ImageField(upload_to='photos/crousel')
    card_1_3 = models.ImageField(upload_to='photos/crousel')
    
    card_2_1 = models.ImageField(upload_to='photos/crousel')
    card_2_2 = models.ImageField(upload_to='photos/crousel')
    card_2_3 = models.ImageField(upload_to='photos/crousel')
    
    card_3_1 = models.ImageField(upload_to='photos/crousel')
    card_3_2 = models.ImageField(upload_to='photos/crousel')
    card_3_3 = models.ImageField(upload_to='photos/crousel')
    
    def __str__(self) :
        return self.Imgaes_of_home