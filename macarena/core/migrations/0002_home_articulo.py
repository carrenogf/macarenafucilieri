# Generated by Django 4.0.6 on 2022-09-23 00:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='articulo',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]