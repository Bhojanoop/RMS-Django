# Generated by Django 4.1.7 on 2023-08-24 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_brand_service', '0004_rename_brand_roles_id_brandroles_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brandverification',
            old_name='govt_doc',
            new_name='govt_doc_filename',
        ),
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.CharField(default=1692868446.749424, max_length=50),
        ),
        migrations.AlterField(
            model_name='brandroles',
            name='created_at',
            field=models.CharField(default=1692868446.755425, max_length=50),
        ),
        migrations.AlterField(
            model_name='brandverification',
            name='created_at',
            field=models.CharField(default=1692868446.753424, max_length=50),
        ),
    ]
