# Generated by Django 3.0.5 on 2020-05-08 14:26

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20200508_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_phone_pure',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
        migrations.AlterField(
            model_name='flat',
            name='construction_year',
            field=models.IntegerField(db_index=True, null=True, verbose_name='Год постройки здания'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='pure_phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]