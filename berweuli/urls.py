from django.urls import path
from berweuli.views import menu

urlpatterns = [
    path('menu', menu)
]
