# Generated by Django 3.0.5 on 2020-05-08 12:39

from django.db import migrations


def bind_owners_and_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owner, _ = Owner.objects.get_or_create(name=flat.owner, pure_phonenumber=flat.owner_phone_pure)
        owner.flats_in_property.set([flat])
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20200507_1944'),
    ]

    operations = [
        migrations.RunPython(bind_owners_and_flats)
    ]