# Generated by Django 3.0.5 on 2020-05-07 16:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0014_auto_20200507_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
