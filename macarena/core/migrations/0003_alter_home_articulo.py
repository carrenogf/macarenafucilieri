# Generated by Django 4.0.6 on 2022-09-23 00:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_home_articulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='articulo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]