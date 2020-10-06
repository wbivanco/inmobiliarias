from django.contrib import admin

from inmueble.models import Servicio, Casa


class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo', 'fecha_creacion']
    list_filter = ['activo']
    search_fields = ['nombre']
    actions = ['desactivar', 'activar']

    def desactivar(self, request, queryset):
        queryset.update(activo=False)

    desactivar.short_description = 'Acción para desactivar los servicios'

    def activar(self, request, queryset):
        queryset.update(activo=True)

    activar.short_description = 'Activar servicios'


admin.site.register(Servicio, ServicioAdmin)


@admin.register(Casa)
class CasaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_creacion', 'usuario', 'inmobiliaria', 'obtener_servicios']
    autocomplete_fields = ['servicios']
    list_filter = ['servicios', 'en_alquiler', 'en_venta']
    list_select_related = ['usuario', 'inmobiliaria']

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()

    def obtener_servicios(self, casa):
        return ", ".join(list(casa.servicios.values_list('nombre', flat=True)))

    obtener_servicios.short_description = 'Servicios'

    def get_queryset(self, request):
        return super().get_queryset(request)