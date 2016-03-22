# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='co',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('Nombre', models.CharField(max_length=20)),
                ('Apellido', models.CharField(max_length=20)),
                ('Telefono', models.CharField(max_length=20)),
            ],
        ),
    ]
