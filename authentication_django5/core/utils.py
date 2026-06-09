import secrets
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from core.permission_config import PERMISSION_CONFIG
from account.models import User

def assign_permissions(user: User):
    role_permissions = PERMISSION_CONFIG.get(user.role, {})
    for model, perms in role_permissions.items():
        content_type = ContentType.objects.get_for_model(model)
        for perm_codename in perms:
            permission_codename = f"{perm_codename}_{model._meta.model_name}"
            try:
                permission = Permission.objects.get(codename=permission_codename, content_type=content_type)
                user.user_permissions.add(permission)
            except Permission.DoesNotExist:
                print(f"Permission {permission_codename} does not exist.")

def generate_otp():
    return str(secrets.randbelow(900000) + 100000)