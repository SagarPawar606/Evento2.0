from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    
    # fields to display in admin panel for a specific user 
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("name","bio","profile_pic","location","organizer","facebook","instagram","twitter","website")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    # fields which will be used for new user creation
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "name","password1", "password2"),
            },
        ),
    )
    search_fields = ("email",)
    list_display = ("name", "email", "is_staff", "is_superuser")
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)