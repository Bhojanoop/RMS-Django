# Generated by Django 4.1.7 on 2023-09-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_brand_service', '0014_brand_verified_by_alter_brand_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.CharField(default=1694270667.81753, max_length=50),
        ),
        migrations.AlterField(
            model_name='brandroles',
            name='created_at',
            field=models.CharField(default=1694270667.836533, max_length=50),
        ),
        migrations.AlterField(
            model_name='brandverification',
            name='created_at',
            field=models.CharField(default=1694270667.832533, max_length=50),
        ),
    ]
