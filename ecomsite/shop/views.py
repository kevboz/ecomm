from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    products = Product.objects.all()

    #search code
    item_name= request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        products = products.filter(title__icontains=item_name)

    #pagination code
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    products = paginator.get_page(page)  

    return render(request, 'shop/index.html', {'products': products})

def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product': product})
