from django.db import models
from autoslug import AutoSlugField


class CategoryModel(models.Model):
    order = models.IntegerField(
        default=0,
        help_text='Kategorilerin sıralanması için buradan sıra numarası verilmesi gerekiyor.',
    )
    name = models.CharField(max_length=100, blank=False, null=False,)
    slug = AutoSlugField(populate_from='name', unique=True)
    categoryData = models.CharField(max_length=100, blank=False, null=False)
    menuData = models.CharField(max_length=100, blank=False, null= False)

    class Meta:
        db_table = 'Kategori'
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'
        ordering = ('order', )

    def __str__(self):
        return self.name

    # public int CategoryID { get; set; }
    #     public string ImageUrl { get; set; }
    #     public string Title { get; set; }
    #     public string? TitleEn { get; set; }
    #     public string? TitleAe { get; set; }
    #     public string? categoryData { get; set; }
    #     public string MenuData { get; set; }

    #     public List<Food> Foods { get; set; }