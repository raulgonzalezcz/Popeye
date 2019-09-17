from django.db import models

def get_image_filename(instance, filename):
    ext = filename.split('.')[-1]
    folder = instance.nombre
    filename = '{}.{}'.format("Logotipo", ext)
    return "images/%s/%s" % (folder, filename)

def get_images_filename(instance, filename):
    ext = filename.split('.')[-1]
    folder = instance.establecimiento
    filename = '{}.{}'.format("Imagen", ext)
    return "images/%s/%s" % (folder, filename)

# Create your models here.
class Tipo_Usuario(models.Model):
    nombre_tipo = models.CharField(max_length=100)

    # this function will be invoked when this model object is foreign key of other model(for example Employee model.).
    def __str__(self):
        text = self.nombre_tipo
        return text


class Usuario(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    apellidos = models.CharField(max_length=100, blank=False)
    correo_electronico = models.EmailField(max_length=150, blank=False)
    telefono = models.CharField(max_length=100, blank=False)
    contrasena = models.CharField(max_length=100, blank=False)
    id_tipo_usuario = models.ForeignKey(Tipo_Usuario, on_delete=models.CASCADE)
    """
    pais = 
    estado =
    ciudad =
    """

    def __str__(self):
        text = self.apellidos + self.nombre
        return text

class Conductor(models.Model):
    id_tipo_usuario = models.ForeignKey(Tipo_Usuario, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    #

class Establecimiento(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    
    def get_name(self):
        text = self.nombre
        return text

    logotipo = models.ImageField(upload_to=get_image_filename, blank=False)
    """
    tipo_establecimiento =
    tipo_comida = 
    """
    descripcion = models.CharField(max_length=250, blank=False)
    recomendacion= models.CharField(max_length=250, blank=False)
    descuento_popeyes = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    pago_conductores = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    telefono = models.CharField(max_length=100, blank=False)
    """
    direccion = 
    pais =
    estado = 
    ciudad =
    horarios =
    """
    marcador_mapa = models.CharField(max_length=100, blank=False)
    ImagenesEstablecimiento = None

    def __str__(self):
        text = self.nombre
        return text

class ImagenesEstablecimiento(models.Model):
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, default=None)
    imagen = models.ImageField(upload_to=get_images_filename, blank=False)


