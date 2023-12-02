from django.shortcuts import render
from berweuli.models import MenuModel, SauceModel

def menu_icerik(request):
    menuler = MenuModel.objects.all()
    sauces = SauceModel.objects.all()
    return render(request, 'pages/menu_icerik.html', context={
        'menuler': menuler,
        'sauces': sauces
        })