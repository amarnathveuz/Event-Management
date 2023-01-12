from django.contrib import admin

# Register your models here.

from .models import company_User,company_Master,company_Role_Master,company_Role_Nav_Master,event_Creation,Event_note


admin.site.register(company_User)
admin.site.register(company_Master)
admin.site.register(company_Role_Master)
admin.site.register(company_Role_Nav_Master)
admin.site.register(event_Creation)
admin.site.register(Event_note)
