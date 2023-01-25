from django import template
from django.contrib.auth.models import User


register = template.Library()

from myapp.models import *

@register.filter(name='get_nav_name')
def get_nav_name(value,args):
    data = User.objects.get(id=value.id)
    return data.is_superuser
    

@register.filter(name='notification_count')
def notification_count(value,args):
    data = User.objects.get(id=value.id)
    if data.is_superuser == True:
        data = notification.objects.filter(read_status=False).count()
        return data
        pass
        
    return ''