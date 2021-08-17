# Generated by Django 3.2.6 on 2021-08-17 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TTK', '0008_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='BLOG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Date_Created', models.DateTimeField(default=datetime.datetime.now)),
                ('Image', models.ImageField(upload_to='Blogs')),
                ('Description', models.TextField()),
            ],
        ),
    ]