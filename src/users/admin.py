from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
   fieldsets = (
        (None, {
            'fields': ('username', 'password', "discount")
        }),
        ('Персональная информация', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Права доступа', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Важные даты', {
            'fields': ('last_login', 'date_joined')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)