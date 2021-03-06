# Generated by Django 3.0.5 on 2021-04-05 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('changed_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('first_name', models.CharField(max_length=255, unique=True)),
                ('last_name', models.CharField(max_length=255, unique=True)),
                ('cell_number', models.IntegerField(blank=True, null=True)),
                ('_type', models.CharField(choices=[('monthly', 'Monthly'), ('quarterly', 'Quarterly'), ('yearly', 'Yearly'), ('lifetime', 'Lifetime')], max_length=255, unique=True)),
                ('days', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'abstract': False,
                'default_permissions': [],
            },
        ),
    ]
