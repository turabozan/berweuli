from berweuli.models import MenuModel, CategoryModel
from modeltranslation.translator import TranslationOptions,register

@register(MenuModel)
class MenuTranslationOptions(TranslationOptions):
    fields = ('name', 'content')

# @register(CategoryModel)
# class CategoryTranslationOptions(TranslationOptions):
#     fields = ('name',)