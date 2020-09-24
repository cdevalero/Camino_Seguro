from django.db import models

class Lugares_Dir(models.Model):
    LUGAR = (
        ('c','ciudad'),
        ('e','estado'),
    )
    nombre = models.CharField(null=False, verbose_name='Nombre', max_length=255)
    tipo = models.CharField(max_length=1, choices=LUGAR, null=False, verbose_name='Tipo')
    id_lugar = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank = True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'lugar_dir'
        verbose_name = 'Lugar/Direcion'
        verbose_name_plural = 'Lugares/Direciones'
        ordering = ['id']

class Companias(models.Model):
    codigo = models.IntegerField(null=False, verbose_name='Codigo', unique=True)
    nombre = models.CharField(null=False, verbose_name='Nombre', max_length=255, unique=True)
    calleav = models.CharField(null=False, verbose_name='Calle/Avenida', max_length=255)
    id_ciudad = models.ForeignKey(Lugares_Dir, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'companias'
        verbose_name = 'Compañia'
        verbose_name_plural = 'Compañias'
        ordering = ['id']

class Particulares(models.Model):
    LICENCIA = (
        (4,'Tipo 4'),
        (5,'Tipo 5'),
    )
    dni = models.IntegerField(null=False, verbose_name='DNI', unique=True)
    nombre = models.CharField(null=False, verbose_name='Nombre', max_length=255)
    apellido1 = models.CharField(null=False, verbose_name='Apellido 1', max_length=255)
    apellido2 = models.CharField(null=False, verbose_name='Apellido 2', max_length=255)
    calleav = models.CharField(null=False, verbose_name='Calle/Avenida', max_length=255)
    tip_lic = models.IntegerField(max_length=1, choices=LICENCIA, null=False, verbose_name='Tipo de licencia')
    fecha_exp = models.DateField(verbose_name='Fecha expiracion', null=False)
    riesgo = models.BooleanField(verbose_name='Riesgo', null=True, blank = True)
    id_ciudad = models.ForeignKey(Lugares_Dir, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nombre + ' ' + self.apellido1 + ' ' + self.apellido2
    
    class Meta:
        db_table = 'particulares'
        verbose_name = 'Particular'
        verbose_name_plural = 'particulares'
        ordering = ['id']

class Oficinas(models.Model):
    nombre = models.CharField(null=False, verbose_name='Nombre', max_length=255, unique=True)
    calleav = models.CharField(null=False, verbose_name='Calle/Avenida', max_length=255)
    id_ciudad = models.ForeignKey(Lugares_Dir, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'oficinas'
        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'
        ordering = ['id']

class Camiones(models.Model):
    MTS = (
        (18, '18 mts'),
        (12, '12 mts'),
        (5, '5 mts'),
    )
    num_registro = models.IntegerField(verbose_name='Numero de registro', unique=True, null=False)
    fecha_exp = models.DateField(verbose_name='Vencimiento de registro', null=False)
    fecha_man = models.DateField(verbose_name='Mantenimiento', null=False)
    tammts = models.IntegerField(verbose_name='Tamaño (mts)', null=False, choices=MTS)
    km = models.IntegerField(verbose_name='Km actual', null=False)
    capacidad = models.IntegerField(verbose_name='Capacidad', null=False)
    radio = models.BooleanField(verbose_name='Radio', null=True, blank = True)
    id_oficina = models.ForeignKey(Oficinas, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.num_registro)
    
    class Meta:
        db_table = 'camiones'
        verbose_name = 'Camion'
        verbose_name_plural = 'Camiones'
        ordering = ['id']

class Remolques(models.Model):
    MTS = (
        (4, '4 mts'),
        (2, '2 mts'),
    )
    num_registro = models.IntegerField(verbose_name='Numero de registro', unique=True, null=False)
    fecha_exp = models.DateField(verbose_name='Vencimiento de registro', null=False)
    fecha_man = models.DateField(verbose_name='Mantenimiento', null=False)
    tammts = models.IntegerField(verbose_name='Tamaño (mts)', null=False, choices=MTS)
    material = models.CharField(verbose_name='Material', null=False, max_length=255)
    abierto = models.BooleanField(verbose_name='Abierto', null=True, blank = True)
    id_oficina = models.ForeignKey(Oficinas, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.num_registro)
    
    class Meta:
        db_table = 'remolques'
        verbose_name = 'Remolque'
        verbose_name_plural = 'Remolques'
        ordering = ['id']

class Contrartos(models.Model):
    fecha_alquiler = models.DateField(verbose_name='Alquiler', null=False)
    dura = models.IntegerField(verbose_name='Duracion', null=False)
    deposito = models.IntegerField(verbose_name='Deposito', null=False)
    tar_dia = models.IntegerField(verbose_name='Tarifa/Dia', null=False)
    id_ofic_origen = models.ForeignKey(Oficinas, on_delete=models.CASCADE, null=False, related_name='id_ofic_origen')
    id_ofic_destino = models.ForeignKey(Oficinas, on_delete=models.CASCADE, null=False, related_name='id_ofic_destino')
    id_camion = models.ForeignKey(Camiones, on_delete=models.CASCADE, null=True, blank = True)
    id_remolque = models.ForeignKey(Remolques, on_delete=models.CASCADE, null=True,blank = True)
    id_compa = models.ForeignKey(Companias, on_delete=models.CASCADE, null=True, blank = True)
    id_per = models.ForeignKey(Particulares, on_delete=models.CASCADE, null=True, blank = True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'contratos'
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        ordering = ['id']