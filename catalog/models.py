from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    slug = models.SlugField(verbose_name='Slug', max_length=100)

    created = models.DateTimeField(verbose_name='Created at',auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Modified at',auto_now=True)

    class Meta:
        verbose_name='Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("catalog:category_products", kwargs={"slug": self.slug})
    
class Product(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    slug = models.SlugField(verbose_name='Slug', max_length=100)
    description = models.TextField(verbose_name='Description', blank=True)
    price = models.DecimalField(verbose_name='Price',max_digits=10, decimal_places=2)

    created = models.DateTimeField(verbose_name='Created at',auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Modified at',auto_now=True)

    category = models.ForeignKey('catalog.Category', verbose_name='Category',on_delete=models.CASCADE)

    class Meta:
        verbose_name='Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"slug": self.slug})
    
    