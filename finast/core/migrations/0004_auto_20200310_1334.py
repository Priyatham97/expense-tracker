# Generated by Django 3.0.3 on 2020-03-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200310_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]