# Generated by Django 4.1.2 on 2022-10-27 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='large_picture',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='bot',
            name='small_picture',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
