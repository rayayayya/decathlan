import datetime
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from main.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags


@login_required(login_url='/login')
def show_main(request):
    """Display products with filter (all or my products)"""
    context = {
        'npm': '2406400373',
        'name': request.user.username,
        'class': 'PBP D',
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)


@csrf_exempt
@require_POST
def create_product(request):
    """Create a new product (AJAX)"""
    try:
        name = strip_tags(request.POST.get("name", ""))
        price = request.POST.get("price")
        description = strip_tags(request.POST.get("description", ""))
        category = request.POST.get("category", "other")
        thumbnail = request.POST.get("thumbnail", "")
        stock = request.POST.get("stock", 0)
        brand = strip_tags(request.POST.get("brand", ""))
        user = request.user

        new_product = Product(
            name=name,
            price=price,
            description=description,
            category=category,
            thumbnail=thumbnail,
            stock=stock,
            brand=brand,
            user=user
        )
        new_product.save()
        return HttpResponse(b"CREATED", status=201)
    except Exception as e:
        print(f"Error creating product: {e}")
        return HttpResponse(b"ERROR", status=400)


@csrf_exempt
@require_POST
def edit_product(request, id):
    """Edit an existing product (AJAX)"""
    try:
        product = get_object_or_404(Product, pk=id)

        product.name = strip_tags(request.POST.get("name", product.name))
        product.price = request.POST.get("price", product.price)
        product.description = strip_tags(request.POST.get("description", product.description))
        product.category = request.POST.get("category", product.category)
        product.thumbnail = request.POST.get("thumbnail", product.thumbnail)
        product.stock = request.POST.get("stock", product.stock)
        product.brand = strip_tags(request.POST.get("brand", product.brand))

        product.save()
        return HttpResponse(b"UPDATED", status=200)
    except Exception as e:
        print(f"Error editing product: {e}")
        return HttpResponse(b"ERROR", status=400)


@csrf_exempt
@require_POST
def delete_product(request, id):
    """Delete a product (AJAX)"""
    try:
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return HttpResponse(b"DELETED", status=200)
    except Exception as e:
        print(f"Error deleting product: {e}")
        return HttpResponse(b"ERROR", status=400)


@login_required(login_url='/login')
def show_products(request, id):
    """Show product details"""
    product = get_object_or_404(Product, pk=id)
    product.increment_views()
    
    context = {
        'product': product
    }
    return render(request, "product_details.html", context)


def show_json(request):
    """Get all products as JSON"""
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': float(product.price),
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'stock': product.stock,
            'brand': product.brand,
            'product_views': product.product_views,
            'user_id': product.user_id,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)


def show_xml(request):
    """Get all products as XML"""
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json_by_id(request, product_id):
    """Get specific product as JSON"""
    try:
        product = Product.objects.get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': float(product.price),
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'stock': product.stock,
            'brand': product.brand,
            'product_views': product.product_views,
            'user_id': product.user_id,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)


def show_xml_by_id(request, product_id):
    """Get specific product as XML"""
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)


def register(request):
    """User registration"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'register.html', context)


@csrf_exempt
def login_user(request):
    """User login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')


def logout_user(request):
    """User logout"""
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response