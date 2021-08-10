# Generated by Django 3.2.4 on 2021-07-30 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('identify', models.CharField(blank=True, choices=[('CED', 'CÉDULA'), ('RUC', 'REGISTRO UNICO CONTRIBUYENTE'), ('PAS', 'PASAPORTE')], max_length=13, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.FileField(blank=True, max_length=255, null=True, upload_to='perfil/%Y/%m/%d')),
                ('is_active', models.BooleanField(default=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'tbl_usuario',
            },
        ),
        migrations.CreateModel(
            name='Entrepreneur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_mies', models.CharField(blank=True, db_column='codigo_mies', max_length=45, null=True, verbose_name='Código MIES')),
                ('phone', models.CharField(blank=True, db_column='telefono', max_length=10, null=True, verbose_name='Teléfono')),
                ('phone2', models.CharField(blank=True, db_column='telefono2', max_length=10, null=True, verbose_name='Teléfono 2')),
                ('neighborhood', models.CharField(blank=True, db_column='barrio', max_length=200, null=True, verbose_name='Barrio')),
                ('sector', models.CharField(blank=True, db_column='sector', max_length=60, null=True, verbose_name='Sector')),
                ('address', models.CharField(blank=True, db_column='domicilio', max_length=255, null=True, verbose_name='Domicilio')),
                ('user', models.ForeignKey(db_column='usuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_emprendedor',
            },
        ),
        migrations.CreateModel(
            name='Entrepreneurship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(blank=True, db_column='latitud', max_length=45, null=True, verbose_name='Latitud')),
                ('length', models.CharField(blank=True, db_column='longitud', max_length=45, null=True, verbose_name='Longitud')),
                ('code', models.CharField(blank=True, db_column='codigo', max_length=45, null=True, verbose_name='Código')),
                ('address', models.CharField(blank=True, db_column='direccion', max_length=255, null=True, verbose_name='Dirección')),
                ('status', models.BooleanField(blank=True, db_column='estado', default=True, null=True, verbose_name='Etado')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
                'db_table': 'tbl_emprendimiento',
            },
        ),
        migrations.CreateModel(
            name='MiesStorageValidated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_base_mies', models.IntegerField(blank=True, db_column='#-Base-MIES', null=True)),
                ('identify', models.TextField(blank=True, db_column='CEDULA', null=True)),
                ('names', models.TextField(blank=True, db_column='APELLIDOS Y NOMBRES', null=True)),
                ('phone', models.TextField(blank=True, db_column='TELEFONO', null=True)),
                ('email', models.TextField(blank=True, db_column='Correos electrónicos', null=True)),
                ('sector', models.TextField(blank=True, db_column='SECTOR', null=True)),
                ('neighborhood', models.TextField(blank=True, db_column='Barrio', null=True)),
                ('address', models.TextField(blank=True, db_column='Domicilio', null=True)),
                ('type_act_econ', models.TextField(blank=True, db_column='TipoActEcon', null=True)),
                ('economic_activity', models.TextField(blank=True, db_column='ACTIVIDAD ECONOMICA', null=True)),
                ('is_active', models.TextField(blank=True, db_column='Act-Activa', null=True)),
                ('bond_reception_date', models.TextField(blank=True, db_column='FECHA de RECEPCIÓN DE BONO', null=True)),
                ('observations_mies', models.TextField(blank=True, db_column='OBSERVACIONES MIES', null=True)),
                ('observations_sociology', models.TextField(blank=True, db_column='OBSERVACIONES SOCIOLOGÍA', null=True)),
                ('student_sociology', models.TextField(blank=True, db_column='Estudiante  Sociología', null=True)),
            ],
            options={
                'db_table': 'stage_mies_validada',
            },
        ),
        migrations.CreateModel(
            name='TypeActivityEconomic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_column='nombre', max_length=100, null=True, unique=True)),
                ('description', models.CharField(blank=True, db_column='descripcion', max_length=255, null=True)),
                ('created_date', models.TimeField(auto_now_add=True, db_column='fecha_creacion')),
                ('updated_date', models.TimeField(auto_now=True, db_column='fecha_edicion')),
            ],
            options={
                'verbose_name': 'name',
                'verbose_name_plural': 'Tipo Actividad Económica',
                'db_table': 'tbl_tipo_actividad_economica',
            },
        ),
        migrations.CreateModel(
            name='Observations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(blank=True, db_column='detalle', max_length=100, null=True)),
                ('observation_type', models.CharField(blank=True, db_column='tipo_observacion', max_length=255, null=True)),
                ('entrepreneurship', models.ForeignKey(db_column='emprendimiento', on_delete=django.db.models.deletion.CASCADE, to='entrepreneur.entrepreneurship')),
            ],
            options={
                'verbose_name': 'Bono',
                'verbose_name_plural': 'Bonos',
                'db_table': 'tbl_observaciones',
            },
        ),
        migrations.AddField(
            model_name='entrepreneurship',
            name='economic_activity',
            field=models.ForeignKey(db_column='actividad_economica', on_delete=django.db.models.deletion.CASCADE, to='entrepreneur.typeactivityeconomic'),
        ),
        migrations.AddField(
            model_name='entrepreneurship',
            name='entrepreneur',
            field=models.ForeignKey(db_column='emprendedor', on_delete=django.db.models.deletion.CASCADE, to='entrepreneur.entrepreneur'),
        ),
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reception', models.DateField(blank=True, db_column='fecha_recepcion', null=True, verbose_name='Fecha de Recepción')),
                ('value', models.FloatField(blank=True, db_column='valor', null=True)),
                ('description', models.CharField(blank=True, db_column='descripcion', max_length=255, null=True)),
                ('entrepreneurship', models.ForeignKey(db_column='emprendimiento', on_delete=django.db.models.deletion.CASCADE, to='entrepreneur.entrepreneurship')),
            ],
            options={
                'verbose_name': 'Bono',
                'verbose_name_plural': 'Bonos',
                'db_table': 'tbl_bono',
            },
        ),
        migrations.CreateModel(
            name='ActivityEconomic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_column='nombe', max_length=100, null=True, unique=True, verbose_name='Nombre')),
                ('description', models.CharField(blank=True, db_column='descripcion', max_length=255, null=True, verbose_name='Descripción')),
                ('typeActEcon', models.ForeignKey(db_column='tipo_act_economica', on_delete=django.db.models.deletion.CASCADE, to='entrepreneur.typeactivityeconomic')),
            ],
            options={
                'verbose_name': 'Actividad Económica',
                'verbose_name_plural': 'Actividades Económicas',
                'db_table': 'tbl_actividad_economica',
            },
        ),
    ]