# Generated by Django 4.0.1 on 2022-02-06 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_id_product__id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='_id',
            new_name='id',
        ),
    ]
