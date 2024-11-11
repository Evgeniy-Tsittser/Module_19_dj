from django.urls import path
from .views import home_page, shop_page, cart_page, sign_up_by_django, hello_message

urlpatterns = [
    path('', home_page),
    path('shop/', shop_page),
    path('cart/', cart_page),
    path('django_sign_up/', sign_up_by_django),
    path('hello/<str:username>/', hello_message, name='hello_message')
]