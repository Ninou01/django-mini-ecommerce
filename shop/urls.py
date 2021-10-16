from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.shop_page, name='shop_page'),
    path('<slug>', views.produit_page, name='produit_page'),
]
