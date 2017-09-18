# encoding: utf-8

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField('Description', blank=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


