# Generated by Django 3.1.1 on 2020-09-21 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alquiler', '0003_auto_20200921_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camiones',
            name='id_oficina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquiler.oficinas'),
        ),
        migrations.AlterField(
            model_name='contrartos',
            name='id_camion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alquiler.camiones'),
        ),
        migrations.AlterField(
            model_name='contrartos',
            name='id_compa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alquiler.companias'),
        ),
        migrations.AlterField(
            model_name='contrartos',
            name='id_ofic_destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_ofic_destino', to='alquiler.oficinas'),
        ),
        migrations.AlterField(
            model_name='contrartos',
            name='id_ofic_origen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_ofic_origen', to='alquiler.oficinas'),
        ),
        migrations.AlterField(
            model_name='contrartos',
            name='id_per',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alquiler.particulares'),
        ),
        migrations.AlterField(
            model_name='contrartos',
            name='id_remolque',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alquiler.remolques'),
        ),
        migrations.AlterField(
            model_name='remolques',
            name='id_oficina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquiler.oficinas'),
        ),
    ]
