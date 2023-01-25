# Generated by Django 4.1.5 on 2023-01-24 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0021_bank_account_master_account_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Booking_user_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(auto_now=True)),
                ('tm', models.TimeField(auto_now=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=25, null=True)),
                ('email', models.CharField(max_length=25, null=True)),
                ('phone', models.CharField(max_length=25, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL)),
                ('event_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Event_Booking_user_Data_event_id', to='myapp.event_creation')),
                ('ticket_type_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Event_Booking_user_Data_ticket_type_id', to='myapp.event_ticket')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event_Booking_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(auto_now=True)),
                ('tm', models.TimeField(auto_now=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=255, null=True)),
                ('order_id', models.CharField(max_length=55, null=True)),
                ('payment_id', models.CharField(max_length=55, null=True)),
                ('total_paid_amount', models.FloatField(null=True)),
                ('received_amount', models.FloatField(null=True)),
                ('payment_status', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL)),
                ('event_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Event_Booking_Table_event_id', to='myapp.event_creation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
