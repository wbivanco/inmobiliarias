from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from util.models import Telefono, RedSocial


class TelefonoInline(GenericTabularInline):
    model = Telefono
    extra = 1
    classes = ['collapse']


class RedSocialInline(GenericTabularInline):
    model = RedSocial
