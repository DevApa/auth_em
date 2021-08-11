from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from auth_em.settings import MEDIA_URL, STATIC_URL


class UsuarioProfileManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Usuario debe tener un email')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)

        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    identify = models.CharField(max_length=13, unique=True, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    image = models.FileField(upload_to='perfil/%Y/%m/%d', max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_evaluator = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UsuarioProfileManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.username

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def __str__(self):
        txt = '{0} con Email: {1}'
        return txt.format(self.username, self.email)

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'tbl_usuario'


class TypeActivityEconomic(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, unique=True, db_column='nombre')
    description = models.CharField(max_length=255, blank=True, null=True, db_column='descripcion')
    created_date = models.TimeField(auto_now_add=True, db_column='fecha_creacion')
    updated_date = models.TimeField(auto_now=True, db_column='fecha_edicion')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_tipo_actividad_economica'
        verbose_name = 'name'
        verbose_name_plural = 'Tipo Actividad Económica'


class ActivityEconomic(models.Model):
    name = models.CharField('Nombre', max_length=100, blank=True, null=True, unique=True, db_column='nombe')
    description = models.CharField('Descripción', max_length=255, blank=True, null=True, db_column='descripcion')
    typeActEcon = models.ForeignKey(TypeActivityEconomic, on_delete=models.CASCADE, db_column='tipo_act_economica')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_actividad_economica'
        verbose_name = 'Actividad Económica'
        verbose_name_plural = 'Actividades Económicas'


class Entrepreneur(models.Model):
    code_mies = models.CharField('Código MIES', max_length=45, blank=True, null=True, db_column='codigo_mies')
    phone = models.CharField('Teléfono', max_length=10, blank=True, null=True, db_column='telefono')
    phone2 = models.CharField('Teléfono 2', max_length=10, blank=True, null=True, db_column='telefono2')
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='usuario')
    neighborhood = models.CharField('Barrio', max_length=200, blank=True, null=True, db_column='barrio')
    sector = models.CharField('Sector', max_length=60, blank=True, null=True, db_column='sector')
    address = models.CharField('Domicilio', max_length=255, blank=True, null=True, db_column='domicilio')

    def __str__(self):
        return self.code_mies()

    class Meta:
        db_table = 'tbl_emprendedor'


class Student(models.Model):
    user = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE, db_column='usuario')
    name = models.CharField('Nombres', max_length=100, blank=True, null=True, db_column='nombre')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_estudiante'
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'


class Entrepreneurship(models.Model):
    latitude = models.CharField('Latitud', max_length=45, blank=True, null=True, db_column='latitud')
    length = models.CharField('Longitud', max_length=45, blank=True, null=True, db_column='longitud')
    code = models.CharField('Código', max_length=45, blank=True, null=True, db_column='codigo')
    address = models.CharField('Dirección', max_length=255, blank=True, null=True, db_column='direccion')
    status = models.BooleanField('Etado', default=True, blank=True, null=True, db_column='estado')
    economic_activity = models.ForeignKey(TypeActivityEconomic, on_delete=models.CASCADE,
                                          db_column='actividad_economica')
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE, db_column='emprendedor')

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'tbl_emprendimiento'
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'


class Bond(models.Model):
    date_reception = models.DateField('Fecha de Recepción', blank=True, null=True, db_column='fecha_recepcion')
    value = models.FloatField(blank=True, null=True, db_column='valor')
    description = models.CharField(max_length=255, blank=True, null=True, db_column='descripcion')
    entrepreneurship = models.ForeignKey(Entrepreneurship, on_delete=models.CASCADE, db_column='emprendimiento')

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'tbl_bono'
        verbose_name = 'Bono'
        verbose_name_plural = 'Bonos'


class MiesStorageValidated(models.Model):
    field_base_mies = models.IntegerField(db_column='#-Base-MIES', blank=True, null=True)
    identify = models.TextField(db_column='CEDULA', blank=True, null=True)
    names = models.TextField(db_column='APELLIDOS Y NOMBRES', blank=True, null=True)
    phone = models.TextField(db_column='TELEFONO', blank=True, null=True)
    email = models.TextField(db_column='Correos electrónicos', blank=True, null=True)
    sector = models.TextField(db_column='SECTOR', blank=True, null=True)
    neighborhood = models.TextField(db_column='Barrio', blank=True, null=True)
    address = models.TextField(db_column='Domicilio', blank=True, null=True)
    type_act_econ = models.TextField(db_column='TipoActEcon', blank=True, null=True)
    economic_activity = models.TextField(db_column='ACTIVIDAD ECONOMICA', blank=True, null=True)
    is_active = models.TextField(db_column='Act-Activa', blank=True, null=True)
    bond_reception_date = models.TextField(db_column='FECHA de RECEPCIÓN DE BONO', blank=True, null=True)
    observations_mies = models.TextField(db_column='OBSERVACIONES MIES', blank=True, null=True)
    observations_sociology = models.TextField(db_column='OBSERVACIONES SOCIOLOGÍA', blank=True, null=True)
    student_sociology = models.TextField(db_column='Estudiante  Sociología', blank=True, null=True)

    class Meta:
        db_table = 'stage_mies_validada'


class Observations(models.Model):
    detail = models.CharField(max_length=100, blank=True, null=True, db_column='detalle')
    entrepreneurship = models.ForeignKey(Entrepreneurship, on_delete=models.CASCADE, db_column='emprendimiento')
    observation_type = models.CharField(max_length=255, blank=True, null=True, db_column='tipo_observacion')

    def __str__(self):
        return self.detail

    class Meta:
        db_table = 'tbl_observaciones'
        verbose_name = 'Bono'
        verbose_name_plural = 'Bonos'
