# Generated by Django 2.2.6 on 2019-10-21 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='avg_rating',
        ),
        migrations.RemoveField(
            model_name='content',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='content',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='content',
            name='reviews_total',
        ),
    ]