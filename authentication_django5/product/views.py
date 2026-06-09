import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product


def require_auth(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Authentication required"}, status=401)


@csrf_exempt
def product_list(request):
    auth_error = require_auth(request)
    if auth_error:
        return auth_error

    if not request.user.has_perm("product.view_product"):
        return JsonResponse({"error": "Forbidden"}, status=403)

    products = list(
        Product.objects.values("id", "name", "description", "price", "created_at", "updated_at")
    )
    return JsonResponse({"products": products}, status=200)


@csrf_exempt
def product_detail(request, product_id):
    auth_error = require_auth(request)
    if auth_error:
        return auth_error

    if not request.user.has_perm("product.view_product"):
        return JsonResponse({"error": "Forbidden"}, status=403)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)

    return JsonResponse({
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": str(product.price),
        "created_at": product.created_at.isoformat(),
        "updated_at": product.updated_at.isoformat(),
    }, status=200)


@csrf_exempt
def product_create(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    auth_error = require_auth(request)
    if auth_error:
        return auth_error

    if not request.user.has_perm("product.add_product"):
        return JsonResponse({"error": "Forbidden"}, status=403)

    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    name = body.get("name")
    description = body.get("description")
    price = body.get("price")

    if not name or not description or price is None:
        return JsonResponse({"error": "name, description and price are required"}, status=400)

    product = Product.objects.create(name=name, description=description, price=price)

    return JsonResponse({
        "message": "Product created successfully",
        "product": {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": str(product.price),
        }
    }, status=201)


@csrf_exempt
def product_update(request, product_id):
    if request.method != "PUT":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    auth_error = require_auth(request)
    if auth_error:
        return auth_error

    if not request.user.has_perm("product.change_product"):
        return JsonResponse({"error": "Forbidden"}, status=403)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)

    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    product.name = body.get("name", product.name)
    product.description = body.get("description", product.description)
    product.price = body.get("price", product.price)
    product.save()

    return JsonResponse({
        "message": "Product updated successfully",
        "product": {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": str(product.price),
        }
    }, status=200)


@csrf_exempt
def product_delete(request, product_id):
    if request.method != "DELETE":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    auth_error = require_auth(request)
    if auth_error:
        return auth_error

    if not request.user.has_perm("product.delete_product"):
        return JsonResponse({"error": "Forbidden"}, status=403)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)

    product.delete()
    return JsonResponse({"message": "Product deleted successfully"}, status=200)
