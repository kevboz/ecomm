from django.shortcuts import render
from .models import Product, Order
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


def checkout(request):
    if request.method == "POST":
        print(request.POST)
        # Here you can add the code to save the order details in the database.
        items= request.POST.get('items', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')   
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')   
        zip = request.POST.get('zip', '')
        total = request.POST.get('total', '')
       
        order = Order(
                    items=items,
                    name=name, 
                    email=email, 
                    address=address,
                    city=city,
                    state=state,
                    zip=zip,
                    total=total
                    )
        order.save()

    return render(request, 'shop/checkout.html')