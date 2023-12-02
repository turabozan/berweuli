from django.db import models
from .category import CategoryModel
from .sauce import SauceModel
from django_resized import ResizedImageField

class ImageQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for obj in self:
            obj.image.delete()
        super(ImageQuerySet, self).delete(*args, **kwargs)

class MenuModel(models.Model):
    objects = ImageQuerySet.as_manager()
    image = ResizedImageField(force_format="WEBP", quality=100, upload_to='menu_images', blank=True, null=True,)
    order = models.IntegerField(
        default=0,
        help_text='Menülerin sıralanması için buradan sıra numarası verilmesi gerekiyor.',
    )
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    content = models.TextField(
        max_length=500,
        blank=True,
    )
    price = models.DecimalField(
        default=0,
        max_digits=5,
        decimal_places=2,
    )

    cookingTime = models.IntegerField(
        default=0,
        help_text='Menünün Hazırlanma süresini giriniz.'
    )

    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        related_name="menu",
    )

    souces = models.ManyToManyField(SauceModel, related_name='souces', blank=True)

    class Meta:
        db_table = 'Menü'
        verbose_name = 'Menü'
        verbose_name_plural = 'Menüler'
        ordering=('order', )

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(MenuModel, self).delete(*args, **kwargs)