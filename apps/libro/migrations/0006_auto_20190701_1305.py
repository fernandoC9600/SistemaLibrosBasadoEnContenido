# Generated by Django 2.2.2 on 2019-07-01 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0005_auto_20190701_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='autor_id',
        ),
        migrations.AddField(
            model_name='libro',
            name='autor_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='libro.Autor'),
            preserve_default=False,
        ),
    ]
