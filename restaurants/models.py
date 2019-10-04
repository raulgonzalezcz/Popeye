from django.db import models

from django.utils.deconstruct import deconstructible

@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sufix = path

    def __call__(self, instance, filename):
        ext = "jpg"
        folder = instance.nombre
        filename = '{}.{}'.format(self.sufix, ext)
        return "images/%s/%s" % (folder, filename)

# Create your models here.
"""
Models to categorize data
"""
class Tipo_usuario(models.Model):
    nombre_tipo = models.CharField(max_length=50)

    # this function will be invoked when this model object is foreign key of other model(for example in model "Usuario")
    def __str__(self):
        text = self.nombre_tipo
        return text

class Tipo_compania(models.Model):
    nombre_compania = models.CharField(max_length=50, blank=False)

    def __str__(self):
        text = self.nombre_compania
        return text

class Tipo_establecimiento(models.Model):
    nombre_establecimiento = models.CharField(max_length=50, blank=False)

    def __str__(self):
        text = self.nombre_establecimiento
        return text

class Tipo_comida(models.Model):
    nombre_comida = models.CharField(max_length=50, blank=False)

    def __str__(self):
        text = self.nombre_comida
        return text

class Tipo_banco(models.Model):
    nombre_banco = models.CharField(max_length=100, blank=False)

    def __str__(self):
        text = self.nombre_banco
        return text

class Super_usuario(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    apellidos = models.CharField(max_length=100, blank=False)
    correo_electronico = models.EmailField(max_length=100, blank=False)
    telefono = models.CharField(max_length=20, blank=False)
    contrasena = models.CharField(max_length=50, blank=False)
    id_tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete=models.CASCADE)

    def __str__(self):
        #text = self.apellidos + ", " + self.nombre + " - " + self.id
        text = self.apellidos + ", " + self.nombre + " - " + self.telefono
        return text

class Base_usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    correo_electronico = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=50)
    id_tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete=models.CASCADE)

    def __str__(self):
        text = self.apellidos + ", " + self.nombre + " - " + self.telefono
        return text

    class Meta:
       abstract = True

class Conductor(Base_usuario):
    codigo_activacion = models.CharField(max_length=6, blank=False)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    tipo_compania = models.ForeignKey(Tipo_compania, on_delete=models.CASCADE)
    #
    pais = models.CharField(max_length=50, blank=False)
    estado = models.CharField(max_length=50, blank=False)
    ciudad = models.CharField(max_length=50, blank=False)
    status = models.CharField(max_length=50, blank=False)

class Establecimiento(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    
    def get_name(self):
        text = self.nombre
        return text

    logotipo = models.ImageField(upload_to=UploadToPathAndRename("Logotipo"), blank=False)
    tipo_establecimiento = models.ForeignKey(Tipo_establecimiento, on_delete=models.CASCADE)
    tipo_comida = models.ForeignKey(Tipo_comida, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=250, blank=False)
    recomendacion= models.CharField(max_length=250, blank=False)

    foto_1 = models.ImageField(upload_to=UploadToPathAndRename("Foto1"), blank=True)
    foto_2= models.ImageField(upload_to=UploadToPathAndRename("Foto2"), blank=True)
    foto_3= models.ImageField(upload_to=UploadToPathAndRename("Foto3"), blank=True)
    foto_4= models.ImageField(upload_to=UploadToPathAndRename("Foto4"), blank=True)
    foto_5= models.ImageField(upload_to=UploadToPathAndRename("Foto5"), blank=True)
    foto_6= models.ImageField(upload_to=UploadToPathAndRename("Foto6"), blank=True)
    foto_7= models.ImageField(upload_to=UploadToPathAndRename("Foto7"), blank=True)
    foto_8= models.ImageField(upload_to=UploadToPathAndRename("Foto8"), blank=True)
    foto_9= models.ImageField(upload_to=UploadToPathAndRename("Foto9"), blank=True)
    foto_10= models.ImageField(upload_to=UploadToPathAndRename("Foto10"), blank=True)
    
    descuento_popeyes = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    pago_conductores = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    telefono = models.CharField(max_length=100, blank=False)

    horario_lunes = models.CharField(max_length=100, blank=False)
    horario_martes = models.CharField(max_length=100, blank=False)
    horario_miercoles = models.CharField(max_length=100, blank=False)
    horario_jueves = models.CharField(max_length=100, blank=False)
    horario_viernes = models.CharField(max_length=100, blank=False)
    horario_sabado = models.CharField(max_length=100, blank=False)
    horario_domingo = models.CharField(max_length=100, blank=False)

    """
    direccion = 
    pais =
    estado = 
    ciudad =
    """
    marcador_mapa = models.CharField(max_length=100, blank=False)

    def __str__(self):
        text = self.nombre
        return text

class Usuario(Base_usuario):
    id_establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
    """
    pais = 
    estado =
    ciudad =
    """

class Calificacion(models.Model):
    id_establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    calificacion = models.IntegerField(default=1,blank=False)
    comentario = models.CharField(max_length=250, blank=False)

    def __str__(self):
        text = str(self.calificacion) + "-" + self.id_usuario.__str__()
        return text

class Respuesta(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    id_calificacion = models.ForeignKey(Calificacion, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=250, blank=False)

    def __str__(self):
        text = self.respuesta
        return text 

class Banco(models.Model):
    id_usuario = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    id_banco = models.ForeignKey(Tipo_banco, on_delete=models.CASCADE)
    numero_cuenta = models.CharField(max_length=100, blank=False)
    rfc = models.CharField(max_length=50, blank=False)
    archivo_key = models.FileField(upload_to='documents/')
    archivo_cot = models.FileField(upload_to='documents/')

class Log_operacion(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    id_establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    cantidad_procesada = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    cantidad_usuario = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    cantidad_popeye = models.DecimalField(max_digits=5, decimal_places=2, blank=False)

class Log_codigo(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    codigo_generado = models.CharField(max_length=50, blank=False)
    id_establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
    id_usuario_genera = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, blank=False)
    id_usuario_recibe = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cantidad_cuenta = models.DecimalField(max_digits=7, decimal_places=2, blank=False)

class Log_saldo(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    id_usuario_recibe = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_usuario_transfiere = models.ForeignKey(Super_usuario, on_delete=models.CASCADE)
    monto_transferido = models.DecimalField(max_digits=7, decimal_places=2, blank=False)

class Log_conver_cu(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    id_usuario_remitente = models.ForeignKey(Conductor, on_delete=models.CASCADE, related_name="remitente")
    id_usuario_destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="destinatario")
    mensaje = models.CharField(max_length=250, blank=False)

class Log_conver_uc(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    id_usuario_remitente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="remitente")
    id_usuario_destinatario = models.ForeignKey(Conductor, on_delete=models.CASCADE, related_name="destinatario")
    mensaje = models.CharField(max_length=250, blank=False)