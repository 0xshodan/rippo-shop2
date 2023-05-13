from django.contrib import admin

from .models import Spacer


@admin.register(Spacer)
class SpacerAdmin(admin.ModelAdmin):
    change_list_template = "spacers_admin.html"
    list_display = ("article", "category", "price20mm", "price30mm", "price40mm", "mount","description")
    list_editable = ("price20mm", "price30mm", "price40mm")
    search_fields = ("article",)
