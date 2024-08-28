from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=225, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    category_image = models.ImageField(
        upload_to='photos/categories', blank=True
    )
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.category_name