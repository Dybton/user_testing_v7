# Generated by Django 2.0.2 on 2019-10-26 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_content_avg_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('readability_rating', models.IntegerField(default=0)),
                ('readability_comments', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='content',
            name='avg_rating',
        ),
    ]