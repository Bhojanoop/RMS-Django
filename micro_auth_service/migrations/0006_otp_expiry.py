# Generated by Django 4.1.7 on 2023-08-26 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_auth_service', '0005_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='expiry',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]