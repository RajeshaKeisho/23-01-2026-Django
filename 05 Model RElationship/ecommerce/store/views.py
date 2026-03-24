from django.shortcuts import render, get_object_or_404
from .models import Customer, Address, Category, Product, Order

# Create your views here.

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'products':products, 'categories':categories})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'category_products.html', {'category':category})

def order_summary(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "order_summary.html", {"order": order})



