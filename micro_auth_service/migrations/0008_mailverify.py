# Generated by Django 4.1.7 on 2023-08-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_auth_service', '0007_vendor_email_verified_at_vendor_registered_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailVerify',
            fields=[
                ('email', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('open_for_verify', models.BooleanField(default=False)),
                ('open_at', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]