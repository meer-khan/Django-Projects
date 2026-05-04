from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
from icecream import ic 
# Create your views here.
@csrf_exempt
def register(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)
    
    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    
    email    = body.get("email")
    password = body.get("password")
    name     = body.get("name")
    city     = body.get("city")
    users = User.objects.all()
    ic(users)
    # convert users to list of dicts
    if not email or not password:
        return JsonResponse({"error": "Email and password are required"}, status=400)
    
    if User.objects.filter(email=email).exists():
        return JsonResponse({"error": "Email already registered"}, status=400)
    
    # user = User.objects.create_user(
    #     email=email,
    #     password=password,
    #     name=name,
    #     city=city
    #     is_active=True,  # Set to True to allow login immediately after registration
    #     is_staff=False,  # Set to True if the user is a staff member
    #    is_superuser=False,  # Set to True if the user is a superuser
    #    is_customer=True,  # Set to True if the user is a customer
    # )
    
    return JsonResponse({
        "message": "User registered successfully",
        "user": {
            # "id":    user.id,
            # "email": user.email,
            # "name":  user.name,
            # "city":  user.city,
        }
    }, status=201)