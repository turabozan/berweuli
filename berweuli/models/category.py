from django.db import models
from autoslug import AutoSlugField


class CategoryModel(models.Model):
    order = models.IntegerField(
        default=0,
        help_text='Kategorilerin sıralanması için buradan sıra numarası verilmesi gerekiyor.',
    )
    name = models.CharField(max_length=100, blank=False, null=False,)
    categoryData = models.CharField(max_length=100, blank=False, null=False)
    menuData = models.CharField(max_length=100, blank=False, null= False)

    class Meta:
        db_table = 'Kategori'
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'
        ordering = ('order', )

    def __str__(self):
        return self.name