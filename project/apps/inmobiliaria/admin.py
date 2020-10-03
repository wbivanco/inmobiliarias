from django.contrib import admin

from inmobiliaria.models import Inmobiliaria
from util.admin import TelefonoInline, RedSocialInline


@admin.register(Inmobiliaria)
class InmobiliariaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo', 'fecha_creacion']
    list_filter = ['activo']
    search_fields = ['nombre']
    inlines = [TelefonoInline, RedSocialInline]