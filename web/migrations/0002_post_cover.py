# Generated by Django 3.0.6 on 2020-05-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
