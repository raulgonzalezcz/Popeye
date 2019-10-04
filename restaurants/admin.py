from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Tipo_usuario)
admin.site.register(Tipo_compania)
admin.site.register(Tipo_establecimiento)
admin.site.register(Tipo_comida)
admin.site.register(Tipo_banco)
admin.site.register(Super_usuario)
admin.site.register(Usuario)
admin.site.register(Conductor)
admin.site.register(Establecimiento)
admin.site.register(Calificacion)
admin.site.register(Respuesta)
admin.site.register(Banco)
admin.site.register(Log_operacion)
admin.site.register(Log_codigo)
admin.site.register(Log_saldo)
admin.site.register(Log_conver_cu)
admin.site.register(Log_conver_uc)

