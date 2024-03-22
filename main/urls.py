from django.urls import path
from .views import *

urlpatterns =[
    path('',index_view , name='index_url'),
    path('account/',account_view , name='account_url'),
]