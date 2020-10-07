from django.conf import settings
from django.db import models


class ModeloBase(models.Model):
    class Meta:
        abstract = True

    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True, editable=False)

    # Auditoria
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        editable=False
    )

    def activar(self):
        self.activo = True
        self.save(update_fields=('activo',))

    def desactivar(self):
        self.activo = False
        self.save(update_fields=('activo', ))
