# Generated by Django 2.0.2 on 2019-10-29 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20191026_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='readability_rating',
        ),
    ]
