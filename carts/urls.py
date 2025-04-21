from django.urls import path
from .views import add_cart, remove_cart_item, decrease_cart_item, cart

urlpatterns = [
    path('', cart, name='cart'),
    path('add/<int:product_id>/', add_cart, name='add_cart'),
    path('remove/<int:product_id>/<int:cart_item_id>/', remove_cart_item, name='remove_cart_item'),
    path('decrease/<int:product_id>/<int:cart_item_id>/', decrease_cart_item, name='decrease_cart_item'),
]
