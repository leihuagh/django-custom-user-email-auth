from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreateForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreateForm
    model = CustomUser
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "life_motto"

                )
            },
        ),
        (
            "Personal Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "life_motto",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    list_display = ["email", "first_name"]
    search_fields = ["email"]
    ordering = ["email"]


admin.site.register(CustomUser, CustomUserAdmin)
