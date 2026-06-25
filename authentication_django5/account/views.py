from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
from icecream import ic
from core.notifications import send_activation_token
from core.utils import generate_otp
from core.utils import assign_permissions
# Create your views here.


@csrf_exempt
def login_user(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    # if request.user.is_authenticated:
    #     return JsonResponse({"error": "User already logged in"}, status=400)

    # if request.method != "POST":
    #     return JsonResponse({"error": "Method not allowed"}, status=405)

    # try:
    #     body = json.loads(request.body)
    # except json.JSONDecodeError:
    #     return JsonResponse({"error": "Invalid JSON"}, status=400)

    # request.POST.get("email") is None because we are sending data in json format and not in form data
    # .POST is used to get data from form data and not from json data
    ic(request.POST.get("email"))
    email = body.get("email")
    ic(email)
    password = body.get("password")

    # if email and password does not exist
    if not email or not password:
        return JsonResponse({"error": "Email and password are required"}, status=400)

    try:
        user = User.objects.get(email=email)
    # ic(user)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

    if not user.is_active:
        return JsonResponse({"error": "User is not active"}, status=400)

    if not user.check_password(password):
        return JsonResponse({"error": "Invalid email or password"}, status=400)

    user = authenticate(request=body, email=email, password=password)
    if user:
        # start session of user in the database
        login(request, user)

    user = User.objects.filter(email=email).first()
    if not user or not user.check_password(password):
        return JsonResponse({"error": "Invalid email or password"}, status=400)

    return JsonResponse({"message": "Login successful"}, status=200)


@csrf_exempt
def register(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    email = body.get("email")
    password = body.get("password")
    name = body.get("name")
    city = body.get("city")
    users = User.objects.all()
    phone = body.get("phone")
    role = body.get("role", "customer")
    ic(users)
    ic(role)
    # convert users to list of dicts
    if not email or not password or not phone:
        return JsonResponse(
            {"error": "Email, password and phone are required"}, status=400
        )

    if User.objects.filter(email=email).exists():
        return JsonResponse({"error": "Email already registered"}, status=400)

    if role is not None and role not in ["customer", "seller"]:
        return JsonResponse({"error": "Invalid role"}, status=400)

    user = User.objects.create_user(
        email=email,
        password=password,
        name=name,
        city=city,
        phone_no=phone,
        is_active=False,  # Set to True to allow login immediately after registration
        is_staff=False,  # Set to True if the user is a staff member
        is_superuser=False,  # Set to True if the user is a superuser
        is_customer=True if role == "customer" else False,  # Set to True if the user is a customer
        is_seller=True if role =="seller" else False,
        role=role,
    )
    ic(user)
    user.save()
    assign_permissions(user)
    token = generate_otp()
    send_activation_token(user_email=email, whatsapp_number=phone, token=token)

    return JsonResponse(
        {
            "message": "User registered successfully",
            "user": {
                # "id":    user.id,
                "email": email,
                "name": name,
                "city": city,
            },
        },
        status=201,
    )


@csrf_exempt
def logout_user(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    # session.flush() is used to delete the session of the user
    request.session.flush()

    return JsonResponse({"message": "Logout successful"}, status=200)


@csrf_exempt
def profile(request):
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    if not request.user.is_authenticated:
        return JsonResponse({"error": "Not authenticated"}, status=401)

    user = request.user

    return JsonResponse(
        {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "city": user.city,
            "phone_no": user.phone_no,
            "is_customer": user.is_customer,
            "is_seller": user.is_seller,
            "created_at": user.created_at.isoformat(),
        },
        status=200,
    )
