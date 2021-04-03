# Generated by Django 3.0.5 on 2020-05-06 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertyrentals', '0002_auto_20200506_1240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agent',
            options={'default_permissions': []},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'default_permissions': []},
        ),
        migrations.AlterModelOptions(
            name='tenant',
            options={'default_permissions': []},
        ),
        migrations.AddField(
            model_name='agent',
            name='changed_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='deleted',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AddField(
            model_name='agent',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='changed_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='deleted',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='changed_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='deleted',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AddField(
            model_name='tenant',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
