from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(company_User)
admin.site.register(company_Master)
admin.site.register(company_Role_Master)
admin.site.register(company_Role_Nav_Master)
admin.site.register(event_Creation)
admin.site.register(Event_note)
admin.site.register(Bank_account_master)
admin.site.register(notification)
admin.site.register(Event_Booking_Table)
admin.site.register(Event_Booking_user_Data)
admin.site.register(Event_booking_user_question_table)
