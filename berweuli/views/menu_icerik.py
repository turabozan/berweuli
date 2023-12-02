from django.shortcuts import render
from berweuli.models import MenuModel, SauceModel, CategoryModel
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

def menu_icerik(request):
    menuler = MenuModel.objects.all()
    sauces = SauceModel.objects.all()
    categories = CategoryModel.objects.all()
    return render(request, 'pages/menu_icerik.html', context={
        'menuler': menuler,
        'sauces': sauces,
        'categories': categories,
        })

def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response