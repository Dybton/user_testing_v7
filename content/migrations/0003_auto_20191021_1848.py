# Generated by Django 2.2.6 on 2019-10-21 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20191021_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='avg_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='content',
            name='reviews_total',
            field=models.IntegerField(default=0),
        ),
    ]
