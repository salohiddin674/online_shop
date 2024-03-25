from django.urls import path
from .views import *

urlpatterns =[
    path('',index_view , name='index_url'),
    path('account/',account_view , name='account_url'),
    path('about/',about_view , name='about_url'),
    path('blog/',blog_view , name='blog_url'),
    path('blog-single/<int:pk>/',blog_single_view , name='blog_single_url'),
    path('cart/',cart_view , name='cart_url'),
    path('checkout/',checkout_view , name='checkout_url'),
    path('contact/',contact_view , name='contact_url'),
    path('create_contact_us/',create_contact_us , name='create_contact_us_url'),
    path('product-single/<int:pk>/',product_single , name='product_single_url'),
    path('shop/',shop_view , name='shop_url'),
    path('wishlist/',wishlist_view , name='wishlist_url'),
    path('create_comment/<int:pk>/', create_comment, name='create_comment_url')


]