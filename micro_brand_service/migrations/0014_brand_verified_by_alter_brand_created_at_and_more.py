# Generated by Django 4.1.7 on 2023-08-30 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('micro_auth_service', '0010_admin_micro_auth__phone_557c52_idx_and_more'),
        ('micro_brand_service', '0013_rename_rolesbrand_rolesforbrand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='verified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='micro_auth_service.admin'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.CharField(default=1693377932.44756, max_length=50),
        ),
        migrations.AlterField(
            model_name='brandroles',
            name='created_at',
            field=models.CharField(default=1693377932.452558, max_length=50),
        ),
        migrations.AlterField(
            model_name='brandverification',
            name='created_at',
            field=models.CharField(default=1693377932.45056, max_length=50),
        ),
    ]
