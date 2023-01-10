from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

password_type = (
    ("Manual","Manual"),
    ("Automatic","Automatic")
)


class common(models.Model):  # COMM0N
    dt = models.DateField(auto_now=True)
    tm = models.TimeField(auto_now=True)
    updated = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=255, null=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="%(app_label)s_%(class)s_ownership", null=True)
    class Meta:
        abstract = True



user_Type = (
    ("company_admin",'company_admin'),
    ("company_staff","company_staff")
)



class company_Master(models.Model):
    company_name = models.CharField(max_length=25,null=True)
    auth_user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name="company_Master_auth_id", null=True)


class company_User(common):
    auth_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="auth_user_login_id", null=True)
    company_name = models.CharField(max_length=25,null=True)
    company_id = models.ForeignKey(company_Master,related_name='company_user_company_master_id',null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=25,null=True)
    username = models.CharField(max_length=25,null=True)
    email = models.CharField(max_length=25,null=True)
    password_option = models.CharField(max_length=25,choices=password_type,null=True)
    phone = models.CharField(max_length=25,null=True)
    photo = models.FileField(upload_to='company_user_photo',null=True)
    user_type = models.CharField(max_length=25,choices=user_Type,default="company_admin")


class category(common):
    name = models.CharField(max_length=255)



class company_Role_Master(common):
    role_name = models.CharField(max_length=25,null=True)
    description  = models.TextField(null=True)
    company_id = models.ForeignKey(company_Master,related_name='company_Role_Master_company_master_id',null=True,on_delete=models.CASCADE)


nav_Nav_Base = (
    ("User Management","User Management"),
    ("Role Management","Role Management"),
    ("Category Management","Category Management"),
    ("Event Management","Event Management"),
    ("Booking Management","Booking Management"),
    ("Notification","Notification")
)
class company_Role_Nav_Master(common):
    role_id = models.ForeignKey(company_Role_Master,related_name='company_Role_Nav_Master_role_id',null=True,on_delete=models.CASCADE)
    nav_name = models.CharField(max_length=25,choices=nav_Nav_Base,null=True)
    Read = models.BooleanField(default=False)
    Write = models.BooleanField(default=False)
    Edit = models.BooleanField(default=False)
    Delete = models.BooleanField(default=False)
    View_All = models.BooleanField(default=False)
    Manage_All = models.BooleanField(default=False)
    
