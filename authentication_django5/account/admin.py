from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.
@admin.register(User)
class UserModelAdmin(UserAdmin):
    model = User
    list_display = (
        "email",
        "name",
        "city",
        "role",
        "is_active",
        "is_staff",
        "is_superuser",
        "is_customer",
        "is_seller",
        "created_at",
        "updated_at",
    )
    list_filter = ("is_active", "is_staff", "is_superuser", "is_customer", "is_seller")
    search_fields = ("email", "name", "city")
    ordering = ("email",)
    readonly_fields = ("created_at", "updated_at")

    # EDIT page
    fieldsets = (
        ("User Credentials", {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("name", "city")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_customer",
                    "is_seller",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    # ADD page
    # add_fieldsets in not a standard ModelAdmin attribute.
    #   UserAdmin overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "name", "city"),
            },
        ),
    )
    # Purpose of filer_horizontal:
    #  When you have a ManyToManyField in your model,
    # Django admin will display it as a multiple select box by default.
    # This can be cumbersome to use when there are many options.
    # By adding the field name to filter_horizontal,
    # Django will display it as a more user-friendly interface with
    # two boxes and arrows to move items between them.
    filter_horizontal = ["groups", "user_permissions"]
