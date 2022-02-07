# Generated by Django 4.0.1 on 2022-02-05 11:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('receipt_id', models.IntegerField(blank=True, null=True)),
                ('receipt_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('inspection_id', models.IntegerField(blank=True, null=True)),
                ('inspection_group', models.CharField(blank=True, max_length=200, null=True)),
                ('inspection_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('inspection_doctor', models.CharField(blank=True, max_length=200, null=True)),
                ('birthday', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('sales_name', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]