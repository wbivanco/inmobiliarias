from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Telefono(models.Model):
    class Meta:
        verbose_name = 'Teléfono'
        verbose_name_plural = 'Teléfonos'

    FIJO = 'fijo'
    CELULAR = 'celular'
    FAX = 'fax'

    TIPOS = (
        (FIJO, 'Teléfono fijo'),
        (CELULAR, 'Celular'),
        (FAX, 'Fax'),
    )

    tipo = models.CharField(max_length=7, choices=TIPOS, default=CELULAR)
    numero = models.CharField(max_length=15)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "{} ({})".format(self.content_object, self.get_tipo_display())


class RedSocial(models.Model):
    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    FACEBOOK = 'facebook'
    INSTAGRAM = 'instagram'

    REDES = (
        (FACEBOOK, 'Facebook'),
        (INSTAGRAM, 'Instagram'),
    )

    red = models.CharField(max_length=9, choices=REDES, default=FACEBOOK)
    url = models.URLField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "{} ({})".format(self.content_object, self.get_red_display())
