# Generated by Django 4.1.5 on 2023-01-10 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_company_user_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='company_Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='company_user',
            name='company_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_user_company_master_id', to='myapp.company_master'),
        ),
    ]
