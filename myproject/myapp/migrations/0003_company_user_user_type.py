# Generated by Django 4.1.5 on 2023-01-10 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_company_user_created_by_company_user_dt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_user',
            name='user_type',
            field=models.CharField(choices=[('company_admin', 'company_admin'), ('company_staff', 'company_staff')], default='company_admin', max_length=25),
        ),
    ]