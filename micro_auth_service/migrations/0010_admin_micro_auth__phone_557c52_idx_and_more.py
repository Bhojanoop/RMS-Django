# Generated by Django 4.1.7 on 2023-08-28 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_auth_service', '0009_alter_otp_otp'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='admin',
            index=models.Index(fields=['phone', 'email'], name='micro_auth__phone_557c52_idx'),
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['phone', 'email'], name='micro_auth__phone_1cdc83_idx'),
        ),
        migrations.AddIndex(
            model_name='vendor',
            index=models.Index(fields=['phone', 'email'], name='micro_auth__phone_413daf_idx'),
        ),
    ]
