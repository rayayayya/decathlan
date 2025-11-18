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
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags


@login_required(login_url='/login')
def show_main(request):
    context = {
        'npm': '2406400373',
        'name': request.user.username,
        'class': 'PBP D',
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'user': request.user
    }
    return render(request, "main.html", context)


@require_POST
def create_product_ajax(request):
    try:
        if not request.user.is_authenticated:
            return JsonResponse({"status": "error", "message": "User not authenticated"}, status=401)

        name = strip_tags(request.POST.get("name", "")).strip()
        price = request.POST.get("price", "")
        description = strip_tags(request.POST.get("description", "")).strip()
        category = request.POST.get("category", "other").strip()
        image = request.POST.get("image", "").strip() or None  
        stock = request.POST.get("stock", 0)
        brand = strip_tags(request.POST.get("brand", "")).strip()
        user = request.user

        if not name:
            return JsonResponse({"status": "error", "message": "Name is required"}, status=400)

        try:
            price_cleaned = str(price).replace('.', '').replace(',', '.')
            price_val = float(price_cleaned) if price_cleaned else 0.0
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Invalid price format: {str(e)}"}, status=400)

        new_product = Product(
            name=name,
            price=price_val,
            description=description,
            category=category,
            thumbnail=image, 
            stock=stock,
            brand=brand,
            user=user
        )
        new_product.save()

        return JsonResponse({
            "status": "success",
            "message": "Product created",
            "product_id": str(new_product.id)
        }, status=201)
    except Exception as e:
        print(f"Error creating product: {e}")
        return JsonResponse({"status": "error", "message": f"Server error: {str(e)}"}, status=500)


@require_POST
def edit_product_ajax(request, id):
    try:
        if not request.user.is_authenticated:
            return JsonResponse({"status": "error", "message": "User not authenticated"}, status=401)

        product = get_object_or_404(Product, pk=id)

        if not (product.user_id == request.user.id):
            return JsonResponse({"status": "error", "message": "Permission denied"}, status=403)

        name = strip_tags(request.POST.get("name", product.name)).strip()
        price = request.POST.get("price", product.price)
        description = strip_tags(request.POST.get("description", product.description)).strip()
        category = request.POST.get("category", product.category)
        image = request.POST.get("image", product.thumbnail)  
        stock = request.POST.get("stock", product.stock)
        brand = strip_tags(request.POST.get("brand", product.brand)).strip()

        try:
            price_cleaned = str(price).replace('.', '').replace(',', '.')
            price_val = float(price_cleaned) if price_cleaned else float(product.price or 0)
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Invalid price format: {str(e)}"}, status=400)

        product.name = name
        product.price = price_val
        product.description = description
        product.category = category
        product.thumbnail = image  
        product.stock = stock
        product.brand = brand

        product.save()
        return JsonResponse({"status": "success", "message": "Product updated"}, status=200)
    except Exception as e:
        print(f"Error editing product: {e}")
        return JsonResponse({"status": "error", "message": f"Server error: {str(e)}"}, status=500)


@require_POST
def delete_product_ajax(request, id):
    """Delete a product (AJAX) -> returns JSON"""
    try:
        if not request.user.is_authenticated:
            return JsonResponse({"status": "error", "message": "User not authenticated"}, status=401)

        product = get_object_or_404(Product, pk=id)

        if not (product.user_id == request.user.id):
            return JsonResponse({"status": "error", "message": "Permission denied"}, status=403)

        product.delete()
        return JsonResponse({"status": "success", "message": "Product deleted"}, status=200)
    except Exception as e:
        print(f"Error deleting product: {e}")
        return JsonResponse({"status": "error", "message": f"Server error: {str(e)}"}, status=500)


def get_product_json(request, id):

    try:
        product = get_object_or_404(Product, pk=id)
        
        if not request.user.is_authenticated:
            return JsonResponse({"status": "error", "message": "User not authenticated"}, status=401)
        
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': float(product.price) if product.price is not None else 0.0,
            'description': product.description,
            'image': product.thumbnail, 
            'category': product.category,
            'stock': product.stock,
            'brand': product.brand,
            'views': product.product_views,
            'user_id': product.user_id,
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=404)


@login_required(login_url='/login')
def show_products(request, id):

    product = get_object_or_404(Product, pk=id)
    try:
        product.increment_views()
    except Exception:
        pass

    context = {'product': product}
    return render(request, "product_details.html", context)


def show_json(request):
    try:
        product_list = Product.objects.all().order_by('-id')
        data = []
        for product in product_list:
            try:
                if isinstance(product.price, str):
                    price_cleaned = product.price.replace('.', '').replace(',', '.')
                    price_value = float(price_cleaned)
                else:
                    price_value = float(product.price) if product.price is not None else 0.0
            except (ValueError, AttributeError, TypeError) as e:
                print(f"Error converting price for product {product.id}: {e}, price value: {product.price}")
                price_value = 0.0
            
            data.append({
                'pk': product.id,
                'fields': {
                    'name': product.name,
                    'price': price_value,
                    'description': product.description or '',
                    'image': product.thumbnail or '',  
                    'category': product.category or 'other',
                    'stock': int(product.stock) if product.stock is not None else 0,
                    'brand': product.brand or '',
                    'views': int(product.product_views) if hasattr(product, 'product_views') and product.product_views is not None else 0,
                    'user': product.user_id,
                }
            })
        return JsonResponse(data, safe=False)
    except Exception as e:
        print(f"Error in show_json: {e}")
        import traceback
        traceback.print_exc()
        return JsonResponse({'error': str(e)}, status=500)


def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json_by_id(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': float(product.price) if product.price is not None else 0.0,
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
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)


def register(request):
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            if is_ajax:
                return JsonResponse({
                    "status": "success",
                    "message": "Account created successfully"
                }, status=201)

            messages.success(request, "Account created!")
            return redirect("main:login")

        if is_ajax:
            return JsonResponse({
                "status": "error",
                "message": "Form invalid",
                "errors": form.errors
            }, status=400)

    form = UserCreationForm()
    return render(request, "register.html", {"form": form})



def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

        if user is not None:
            login(request, user)

            if is_ajax:
                resp = JsonResponse({
                    "status": "success",
                    "message": "Logged in successfully"
                })
                resp.set_cookie('last_login', str(datetime.datetime.now()))
                return resp

            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

        if is_ajax:
            return JsonResponse({
                "status": "error",
                "message": "Invalid username or password"
            }, status=400)
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


@require_POST
def logout_user(request):
    logout(request)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        resp = JsonResponse({"status": "success", "message": "Logged out"})
        resp.delete_cookie('last_login')
        return resp
    else:
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response