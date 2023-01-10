# Generated by Django 4.1.5 on 2023-01-10 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0005_company_master_auth_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='company_Role_Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(auto_now=True)),
                ('tm', models.TimeField(auto_now=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=255, null=True)),
                ('role_name', models.CharField(max_length=25, null=True)),
                ('description', models.TextField(null=True)),
                ('company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_Role_Master_company_master_id', to='myapp.company_master')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='company_Role_Nav_Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(auto_now=True)),
                ('tm', models.TimeField(auto_now=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=255, null=True)),
                ('nav_name', models.CharField(choices=[('User Management', 'User Management'), ('Role Management', 'Role Management'), ('Category Management', 'Category Management'), ('Event Management', 'Event Management'), ('Booking Management', 'Booking Management'), ('Notification', 'Notification')], max_length=25, null=True)),
                ('Read', models.BooleanField(default=False)),
                ('Write', models.BooleanField(default=False)),
                ('Edit', models.BooleanField(default=False)),
                ('Delete', models.BooleanField(default=False)),
                ('View_All', models.BooleanField(default=False)),
                ('Manage_All', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL)),
                ('role_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_Role_Nav_Master_role_id', to='myapp.company_role_master')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
