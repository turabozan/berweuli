from django.contrib import admin
from berweuli.models import CategoryModel, MenuModel, SauceModel
from modeltranslation.admin import TranslationAdmin

@admin.register(CategoryModel)
class CategoryAdmin(TranslationAdmin):
    list_display = ('order', 'name', )


@admin.register(MenuModel)
class MenuAdmin(TranslationAdmin):
    list_display = ('order', 'category', 'name', 'price',)
    list_editable = ('name', 'price',)
    search_fields = ('category__name',)

@admin.register(SauceModel)
class SouceAdmin(TranslationAdmin):
    list_display = ('order','name', )