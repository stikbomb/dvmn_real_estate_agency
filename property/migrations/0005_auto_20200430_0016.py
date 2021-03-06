# Generated by Django 2.2.4 on 2020-04-29 21:16

from django.db import migrations


def get_new_building_status(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if flat.construction_year >= 2015:
            flat.new_building = True
        else:
            flat.new_building = False
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20200430_0006'),
    ]

    operations = [
        migrations.RunPython(get_new_building_status)
    ]
