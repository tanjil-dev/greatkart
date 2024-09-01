from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name   = models.CharField(max_length=50, unique=True)
    slug            = models.SlugField(max_length=100, unique=True)
    description     = models.TextField(max_length=255, blank=True)
    cat_image       = models.ImageField(upload_to='photos/categories/', blank=True)

    class Meta:
        verbose_name        = 'category'
        verbose_name_plural = 'categories'

    def get_urls(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return str(self.category_name)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    subcat_image = models.ImageField(upload_to='photos/subcategories/', blank=True)

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def get_urls(self):
        return reverse('products_by_subcategory', args=[self.slug])

    def __str__(self):
        return str(self.subcategory_name)
