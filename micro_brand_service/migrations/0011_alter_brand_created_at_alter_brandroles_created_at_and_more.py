# Generated by Django 4.1.7 on 2023-08-26 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_brand_service', '0010_alter_brand_created_at_alter_brandroles_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.CharField(default=1693022959.476921, max_length=50),
        ),
        migrations.AlterField(
            model_name='brandroles',
            name='created_at',
            field=models.CharField(default=1693022959.481921, max_length=50),
        ),
        migrations.AlterField(
            model_name='brandverification',
            name='created_at',
            field=models.CharField(default=1693022959.479923, max_length=50),
        ),
    ]
