from django.db import models

'''Modelo base'''
class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField("Estado",default =True)
    fecha_de_creacion = models.DateField("Fecha de Creación", auto_now=False, auto_now_add= True)
    fecha_de_modificacion = models.DateField("Fecha de Modificación", auto_now=True, auto_now_add= False)
    fecha_de_eliminacion = models.DateField("Fecha de Eliminación", auto_now=True, auto_now_add= False)
        
    class Meta:
      abstract =True

'''Modelo que se encarga de registrar los servicios de la empresa'''
class Servicio(ModeloBase):
    nombre_servicio = models.CharField("Nombre del Servicio",max_length=100)
    descripcion_servicio = models.TextField("Descripción del Servicio")
    precio_servicio = models.DecimalField("Precio del Servicio",max_digits=10, decimal_places=2)
    imagen_servicio = models.ImageField("Imagen del Servicio",upload_to="img/", blank=False, null=False)
    
    class Meta:
      verbose_name="Servicio"
      verbose_name_plural="Servicios"

    def __str__(self):
        return self.nombre_servicio
    
'''Modelo que se encarga de registrar los productos de la empresa'''
class Producto(ModeloBase):
    nombre_producto = models.CharField("Nombre del Producto",max_length=100)
    descripcion_producto = models.TextField("Descripción del Producto")
    precio_producto = models.DecimalField("Precio del Producto",max_digits=10, decimal_places=2)
    cantidad_disponible_producto = models.PositiveIntegerField("Cantidad de Productos")
    imagen_producto = models.ImageField("Imagen del Producto",upload_to="img/", blank=False, null=False)
    
    class Meta:
      verbose_name="Producto"
      verbose_name_plural="Productos"

    def __str__(self):
        return self.nombre_producto

'''Modelo que se encarga de registrar las resrvas de los clientes'''
class Reserva(ModeloBase):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, blank=True)
    fecha = models.DateTimeField("Fecha")
    nombre_cliente = models.CharField("Nombre del Cliente",max_length=100)
    telefono_cliente = models.CharField("Teléfono del Cliente",max_length=15)
    correo_cliente = models.EmailField("Correo")
    
    class Meta:
      verbose_name="Reserva"
      verbose_name_plural="Reservas"

    def __str__(self):
        return f'Reserva de {self.servicio.nombre} para {self.nombre_cliente}'
    
'''Modelo que se encarga de registrar la informacion de los clientes'''
class Cliente(ModeloBase):
    nombre_cliente = models.CharField("Nombre del Cliente",max_length=100)
    apellido_cliente = models.CharField("Apellido del Cliente",max_length=100)
    telefono_cliente = models.CharField("Teléfono del Cliente",max_length=15)
    correo_cliente = models.EmailField("Correo")
    
    class Meta:
      verbose_name="Cliente"
      verbose_name_plural="Clientes"

    def __str__(self):
        return f'{self.nombre_cliente} {self.apellido_cliente}'

'''Modelo que se encarga de registrar informacion adicional de la pagina'''
class InformacionPagina(ModeloBase):
    informacion = models.CharField("Información de la página Web",max_length=300)
    acerca = models.TextField("Acerca de la página Web")
    facebook =models.URLField("Facebook", null=True,blank=True)
    instagram =models.URLField("Instagram", null=True,blank=True)
    youtube =models.URLField("YouTube", null=True,blank=True)
    
    class Meta:
      verbose_name="Informacion de la Pagina Web"
      verbose_name_plural="Informacion de la Pagina Web"
    
    def __str__(self):
        return self.informacion

'''Modelo que se encarga de registrar los planes disponibles que ofrece la empresa'''
class Planes(ModeloBase):
    nombre_plan = models.CharField("Nombre del Plan",max_length=100)
    descripcion_plan = models.TextField("Descripción del Plan")
    precio_plan = models.DecimalField("Precio del Plan",max_digits=10, decimal_places=2)
    
    class Meta:
      verbose_name="Plan"
      verbose_name_plural="Planes"

    def __str__(self):
        return self.nombre_plan
    
'''Modelo que se encarga de registrar todos los especialistas de la empresa''' 
class Especialistas(ModeloBase):
    nombre_especialista = models.CharField("Nombre",max_length=100)
    apellido_especialista = models.CharField("Apellido",max_length=100)
    especialidad_especialista = models.CharField("Especialidad",max_length=100)
    telefono_especialista = models.CharField("Teléfono",max_length=15)
    correo_especialista = models.EmailField("Correo")
    foto_especialista= models.ImageField("Foto",upload_to="img/", blank=False, null=False)
    web =models.URLField("Pagina Web", null=True,blank=True)
    facebook =models.URLField("Facebook", null=True,blank=True)
    instagram =models.URLField("Instagram", null=True,blank=True)
    youtube =models.URLField("YouTube", null=True,blank=True)
    class Meta:
      verbose_name="Especialista"
      verbose_name_plural="Especialistas"

    def __str__(self):
        return f'{self.nombre_especialista} {self.apellido_especialista}'
    
'''Modelo que se encarga de registrar las citas de los clientes''' 
class Citas(ModeloBase):
    nombre = models.CharField("Nombre del Cliente",max_length=100)
    correo = models.EmailField("Correo")
    fecha = models.DateField("Fecha")
    hora = models.TimeField("Hora")
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    
    class Meta:
      verbose_name="Cita"
      verbose_name_plural="Citas"

    def __str__(self):
        return self.nombre
        

'''Modelo que se encarga de registrar la informacion de los usuarios'''
class Contactanos(ModeloBase):
    nombre_cliente = models.CharField("Nombre del Cliente",max_length=100)
    apellido_cliente = models.CharField("Apellido del Cliente",max_length=100)
    telefono_cliente = models.CharField("Teléfono del Cliente",max_length=15)
    correo_cliente = models.EmailField("Correo")
    asunto_cliente = models.CharField("Asunto",max_length=100)
    mensaje_cliente = models.TextField("Mensaje")
    
    class Meta:
      verbose_name="Contacto"
      verbose_name_plural="Contactanos"

    def __str__(self):
        return f'{self.nombre_cliente} {self.apellido_cliente}'


class Suscriptor(ModeloBase):
    correo = models.EmailField('Correo Electrónico', max_length = 200)

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.correo