# Generated by Django 4.1.2 on 2022-10-28 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_bot_is_top_bot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='auto_login',
            field=models.BooleanField(default=False),
        ),
    ]
