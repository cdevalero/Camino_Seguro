from django.db import models

class Lugares_Dir(models.Model):
    LUGAR = (
        ('c','ciudad'),
        ('e','estado'),
    )
    nombre = models.CharField(null=False, verbose_name='Nombre')
    tipo = models.CharField(max_length=1, choices=LUGAR, null=False, verbose_name='Tipo')
    id_lugar = models.ForeignKey(Lugares_Dir, on_delete=models.CASCADE)

    class Meta:
        db_table = 'lugar_dir'
        verbose_name = 'Lugar/Direcion'
        verbose_name_plural = 'Lugares/Direciones'
        ordering = ['id']

class Companias(models.Model):
    nombre = models.CharField(null=False, verbose_name='Nombre')
    calleav = models.CharField(null=False, verbose_name='Calle/Avenida')
    id_ciudad = models.ForeignKey(Lugares_Dir, on_delete=models.CASCADE)
    
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
    nombre = models.CharField(null=False, verbose_name='Nombre')
    apellido1 = models.CharField(null=False, verbose_name='Apellido 1')
    apellido2 = models.CharField(null=False, verbose_name='Apellido 2')
    calleav = models.CharField(null=False, verbose_name='Calle/Avenida')
    tip_lic = models.IntegerField(max_length=1, choices=LICENCIA, null=False, verbose_name='Tipo de licencia')
    fecha_exp = models.DateField(verbose_name='Fecha exp', null=False)
    riesgo = models.BooleanField(verbose_name='Riesgo')
    id_ciudad = models.ForeignKey(Lugares_Dir, on_delete=models.CASCADE, null=False)
    
    class Meta:
        db_table = 'particulares'
        verbose_name = 'Particular'
        verbose_name_plural = 'particulares'
        ordering = ['id']

class Oficinas(models.Model):
    
    
    class Meta:
        db_table = 'oficinas'
        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'
        ordering = ['id']

class Camiones(models.Model):
    
    
    class Meta:
        db_table = 'camiones'
        verbose_name = 'Camion'
        verbose_name_plural = 'Camiones'
        ordering = ['id']

class Remolques(models.Model):
    
    
    class Meta:
        db_table = 'remolques'
        verbose_name = 'Remolque'
        verbose_name_plural = 'Remolques'
        ordering = ['id']

class Contrartos(models.Model):
    
    
    class Meta:
        db_table = 'contratos'
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        ordering = ['id']