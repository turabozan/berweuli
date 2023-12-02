from django.db import models


class SauceModel(models.Model):
    order = models.IntegerField(
        default=0,
        help_text='Kategorilerin sıralanması için buradan sıra numarası verilmesi gerekiyor.',
    )
    name = models.CharField(max_length=100, blank=False, null=False,)
    price = models.DecimalField(
        default=0,
        max_digits=5,
        decimal_places=2,
    )

    class Meta:
        db_table = 'Sos'
        verbose_name = 'Sos'
        verbose_name_plural = 'Soslar'
        ordering = ('order', )

    def __str__(self):
        return self.name