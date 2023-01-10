from django import template
from django.contrib.auth.models import User


register = template.Library()

from myapp.models import *

@register.filter(name='get_nav_name')
def get_nav_name(value,args):
    data = User.objects.get(id=value.id)
    return data.is_superuser
    