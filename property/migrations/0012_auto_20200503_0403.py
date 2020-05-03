# Generated by Django 3.0.5 on 2020-05-03 01:03

from django.db import migrations

import phonenumbers


def normalize_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():

        try:
            phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        except phonenumbers.NumberParseException:
            continue

        if phonenumbers.is_valid_number(phonenumber):
            flat.owner_phone_pure = phonenumbers.format_number(phonenumber, phonenumbers.PhoneNumberFormat.E164)
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_flat_owner_phone_pure'),
    ]

    operations = [
        migrations.RunPython(normalize_phonenumber)
    ]