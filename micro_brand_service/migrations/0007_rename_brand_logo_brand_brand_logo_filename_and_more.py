# Generated by Django 4.1.7 on 2023-08-25 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_brand_service', '0006_alter_brand_created_at_alter_brandroles_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='brand_logo',
            new_name='brand_logo_filename',
        ),
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.CharField(default=1692945922.470344, max_length=50),
        ),
        migrations.AlterField(
            model_name='brandroles',
            name='created_at',
            field=models.CharField(default=1692945922.476344, max_length=50),
        ),
        migrations.AlterField(
            model_name='brandverification',
            name='created_at',
            field=models.CharField(default=1692945922.473341, max_length=50),
        ),
    ]
