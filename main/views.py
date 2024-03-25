from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Count
from .models import *

def index_view(request):
    if request.user.is_authenticated:
        user = request.user
        basket = Basket.objects.filter(user_id=user.id).count()
    else:
        basket = 0
    context = {
        'basket': basket,
        'banner':Banner.objects.all().order_by('-id')[:2],
        'category_left':Category.objects.all().order_by('id')[:2],
        'category_right':Category.objects.all().order_by('id')[2:4],
        'product':Product.objects.all().order_by('id')[:8],

    }
    return render(request,'index.html', context)


def account_view(request):
    return render(request, 'account.html')


def about_view(request):
    if request.user.is_authenticated:
        user = request.user
        basket = Basket.objects.filter(user_id=user.id).count()
    else:
        basket = 0
    context = {
        'basket': basket,
        'about':About.objects.last()

    }
    return render(request, 'about.html', context)


def blog_view(request):
    if request.user.is_authenticated:
        user = request.user
        basket = Basket.objects.filter(user_id=user.id).count()
    else:
        basket = 0
    context = {
        'blog':Blog.objects.all().order_by('-id')[:4],
        'category':Category.objects.all().order_by('-id')[:4],
        'tag':Tag.objects.all().order_by('-id')[:7],
        'basket': basket
    }
    return render(request,'blog.html', context)


def blog_single_view(request, pk):
    if request.user.is_authenticated:
        user = request.user
        basket = Basket.objects.filter(user_id=user.id).count()
    else:
        basket = 0
    blog = Blog.objects.get(pk=pk)
    context = {
        'basket': basket,
        'blog': blog,
        'tag': Tag.objects.all().order_by('-id')[:3],
        'comment':Comment.objects.all().order_by('-id')[:3],
        'category': Category.objects.all().order_by('-id')[:4],
        'tag': Tag.objects.all().order_by('-id')[:7],
    }
    return render(request, 'blog-single.html', context)


def cart_view(request):
    if request.user.is_authenticated:
        user = request.user
        basket = Basket.objects.filter(user_id=user.id).count()
    else:
        basket = 0
    product_counts = basket.values('product').annotate(count=Count('id'))
    duplicate_products = [(product_count['product'], product_count['count']) for product_count in product_counts]
    products = []
    for product_id, count in duplicate_products:
        product = Product.objects.get(id=product_id)
        products.append({'name': product,'number': count, 'common': count*product.price})
    total = 0
    for i in products:
        total += i['common']
    context ={
        'products': products,
        'basket': basket.count(),
        'total': total
    }
    return render(request,'cart.html', context)


def checkout_view(request):
    if request.user.is_authenticated:
        user = request.user
        basket = Basket.objects.filter(user_id=user.id).count()
        products = Basket.objects.filter(user_id=user.id)
    else:
        basket = 0
        products = []
    total = 0
    for i in products:
        total += i.product.price
    context = {
        'basket': basket,
        "total": total
    }
    return render(request, 'checkout.html', context)


def contact_view(request):
    if request.user.is_authenticated:
        user = request.user
        basket = Basket.objects.filter(user_id=user.id).count()
    else:
        basket = 0

    contact = Info.objects.last()
    context = {
        'basket': basket,
        'contact': contact
    }
    return render(request,'contact.html', context)


def create_contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ContactUs.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        return redirect('contact_url')


def product_single(request, pk):
    product = Product.objects.get(pk=pk)
    related = Product.objects.filter(category=product.category).order_by('-id')[:4]
    context = {
        'product': product,
        'related': related
    }
    return render(request, 'product-single.html', context)


def shop_view(request):
    categories = Category.objects.all()
    category = request.GET.get('category')
    if category:
        products = Product.objects.filter(category__name=category)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'products': page_obj,
        'selected_category': category
    }
    return render(request, 'shop.html', context)


def wishlist_view(request):
    if request.user.is_authenticated:
        user = request.user
        basket = Basket.objects.filter(user_id=user.id)
    else:
        basket = 0
    product_counts = basket.values('product').annotate(count=Count('id'))
    duplicate_products = [(product_count['product'], product_count['count']) for product_count in product_counts]
    products = []
    for product_id, count in duplicate_products:
        product = Product.objects.get(id=product_id)
        products.append({'name': product,'number': count, 'common': count*product.price})
    total = 0
    for i in products:
        total += i['common']
    basket = Basket.objects.filter(user_id=user.id).count()
    context = {
        'basket': basket,
        'products': products,
        'total': total
    }
    return render(request, 'wishlist.html', context)


def create_comment(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == "POST":
        text = request.POST['text']
        Comment.objects.create(
        user= request.user,
        blog = blog,
        text = text,
        )
    return redirect('blog_single_url', blog.id)