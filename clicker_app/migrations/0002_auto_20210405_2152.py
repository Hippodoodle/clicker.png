# Generated by Django 2.2.17 on 2021-04-05 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clicker_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(default='C:\\workspace\\wadproject\\clicker.png\\media/uploads/logo.jpg', upload_to='uploads/'),
        ),
    ]
