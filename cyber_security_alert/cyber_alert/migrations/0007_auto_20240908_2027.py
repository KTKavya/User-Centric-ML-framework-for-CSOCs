# Generated by Django 3.0.6 on 2024-09-08 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyber_alert', '0006_auto_20240908_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='givertransaction',
            name='gender',
            field=models.CharField(default='None', max_length=4),
        ),
    ]
