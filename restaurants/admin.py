from django.contrib import admin

from .models import *

class PostPictureInline(admin.TabularInline):
    model = ImagenesEstablecimiento
    fields = ['imagen',]


class PostAdmin(admin.ModelAdmin):
    inlines = [PostPictureInline,]

# Register your models here.
admin.site.register(Tipo_Usuario)
admin.site.register(Usuario)
admin.site.register(Conductor)
admin.site.register(Establecimiento)
admin.site.register(ImagenesEstablecimiento)
