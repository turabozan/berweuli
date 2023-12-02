from django.urls import path
from berweuli.views import menu, menu_icerik

urlpatterns = [
    path('menu', menu, name='menu'),
    path('menu_icerik', menu_icerik, name='menu_icerik')
]
