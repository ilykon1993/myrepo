# Generated by Django 2.1.5 on 2019-01-21 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Comment_likes',
            field=models.IntegerField(default=0),
        ),
    ]
