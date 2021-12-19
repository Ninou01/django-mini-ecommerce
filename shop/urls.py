from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop_page, name='shop_page'),
    path('/<produit_id>/<slug>', views.produit_page, name='produit_page'),
]
