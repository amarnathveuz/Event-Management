# Generated by Django 4.1.5 on 2023-01-28 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0030_sponsor_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booth_Category_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(auto_now=True)),
                ('tm', models.TimeField(auto_now=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=255, null=True)),
                ('booth_category', models.CharField(max_length=25, null=True)),
                ('price', models.FloatField(null=True)),
                ('product', models.CharField(max_length=25, null=True)),
                ('company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Booth_Category_type_company_id', to='myapp.company_master')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL)),
                ('sponser_level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Booth_Category_type_sponser_level', to='myapp.sponsor_level')),
                ('sponsor_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Booth_Category_type_sponser_type', to='myapp.sponsor_type')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]