from ecommerce import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'cart_app'
urlpatterns = [
    path('add/<int:product_id>/',views.add_Cart,name='add_cart'),
    path('',views.cart_detail,name='cart_detail'),
    path('remove/<int:product_id>',views.cart_remove,name='cart_remove'),
    path('fullremove/<int:product_id>',views.full_remove,name='full_remove'),

]