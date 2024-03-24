from django.shortcuts import render
from .models import *

def index_view(request):
    return render(request,'index.html')


def account_view(request):
    return render(request, 'account.html')

def about_view(request):
    return render(request, 'about.html')

def blog_view(request):
    context = {
        'blog':Blog.objects.all().order_by('-id')[:6]
    }
    return render(request,'blog.html', context)

def blog_single_view(request):
    return render(request, 'blog-single.html')

def cart_view(request):
    return render(request,'cart.html')

def checkout_view(request):
    return render(request,'checkout.html')

def contact_view(request):
    return render(request,'contact.html')

def product_single(request):
    return render(request,'product-single.html')

def shop_view(request):
    return render(request,'shop.html')

def wishlist_view(request):
    return render(request,'wishlist.html')


