# Generated by Django 2.2.17 on 2021-04-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clicker_app', '0003_auto_20210403_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='image',
            field=models.ImageField(default='C:\\workspace\\wadproject\\clicker.png\\static/images/logo.jpg', upload_to='uploads/'),
        ),
    ]
