# Generated by Django 3.2.6 on 2021-08-17 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TTK', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Image',
            field=models.ImageField(upload_to='Profile'),
        ),
    ]
