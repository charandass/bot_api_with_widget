# Generated by Django 4.1.2 on 2022-10-28 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_bot_large_picture_bot_small_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry_name', models.CharField(max_length=100)),
                ('industry_uuid', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='bot',
            name='industry_uuid',
            field=models.CharField(default=False, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bot',
            name='b2b_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bot',
            name='b2c_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
