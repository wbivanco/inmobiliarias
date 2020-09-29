from django.db import models


class ModeloBase(models.Model):
    class Meta:
        abstract = True

    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True, editable=False)
