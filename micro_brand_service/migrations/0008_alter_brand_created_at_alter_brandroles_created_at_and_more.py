# Generated by Django 4.1.7 on 2023-08-25 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('micro_brand_service', '0007_rename_brand_logo_brand_brand_logo_filename_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.CharField(default=1692946566.483797, max_length=50),
        ),
        migrations.AlterField(
            model_name='brandroles',
            name='created_at',
            field=models.CharField(default=1692946566.488797, max_length=50),
        ),
        migrations.AlterField(
            model_name='brandroles',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brandroles_role', to='micro_brand_service.rolesbrand'),
        ),
        migrations.AlterField(
            model_name='brandverification',
            name='created_at',
            field=models.CharField(default=1692946566.487797, max_length=50),
        ),
    ]
