from django.urls import path
from berweuli.views import menu_icerik

urlpatterns = [
    path('menu', menu_icerik, name='menu')
]