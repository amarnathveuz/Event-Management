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
    

class event_Category(common):
    category_name = models.CharField(max_length=25,null=True)
    company_id = models.ForeignKey(company_Master,related_name='event_Category_company_id',null=True,on_delete=models.CASCADE)
    description = models.TextField(null=True)



import string
import random
from django.utils.text import slugify
def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(1))

class event_Creation(common):
    name = models.CharField(max_length=25,null=True)
    start_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_date = models.DateField(null=True)
    end_time = models.TimeField(null=True)
    image = models.FileField(upload_to='event_image',null=True)
    organizer = models.CharField(max_length=25,null=True)
    responsible = models.CharField(max_length=25,null=True)
    responsible_person_no = models.CharField(max_length=25,null=True)
    company = models.CharField(max_length=25,null=True)
    company_id = models.ForeignKey(company_Master,related_name='event_Creation_company_id',null=True,on_delete=models.CASCADE)
    venue = models.TextField(null=True)
    exhibition_map = models.FileField(upload_to='exhibition_map',null=True)
    limit_registrations = models.BooleanField(default=False)
    limit_registration_no = models.IntegerField(null=True)
    category_id = models.ForeignKey(event_Category,related_name='event_Creation_category_id',null=True,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.name)
        super(event_Creation, self).save(*args, **kwargs)
    

class Event_ticket(common):
    event_id = models.ForeignKey(event_Creation,related_name='Event_ticket_event_id',null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=25,null=True)
    description = models.CharField(max_length=25,null=True)
    product = models.CharField(max_length=25,null=True)
    price = models.FloatField(null=True)
    sale_start_dt = models.DateField(null=True)
    sale_end_dt =  models.DateField(null=True)
    maximum = models.IntegerField(null=True)
    confirmed = models.IntegerField(null=True)
    unconfirmed = models.IntegerField(null=True)


event_question_type = (
    ("Selection","Selection"),
    ("Text Input","Text Input")
)

class Event_question(common):
    event_id = models.ForeignKey(event_Creation,related_name='Event_question_event_id',null=True,on_delete=models.CASCADE)
    question_type = models.CharField(max_length=25,choices=event_question_type,null=True)
    title = models.CharField(max_length=25,null=True)

class Event_selection_question(common):
    Event_question_id =  models.ForeignKey(Event_question,related_name='Event_selection_question_question_id',null=True,on_delete=models.CASCADE)
    answer = models.CharField(max_length=25,null=True)


class Event_note(common):
    event_id = models.ForeignKey(event_Creation,related_name='Event_note_event_id',null=True,on_delete=models.CASCADE)  
    note = models.CharField(max_length=25,null=True)
    ticket_instructions = models.CharField(max_length=25,null=True)



business_type = (
    ("Private Limited","Private Limited"),
    ("Proprietorship","Proprietorship"),
    ("Partnership","Partnership"),
    ("Individual","Individual"),
    ("Public Limited","Public Limited"),
    ("LLP","LLP"),
    ("Trust","Trust"),
    ("Society","Society"),
    ("NGO","NGO")
)

class Bank_account_master(common):
    account_name = models.CharField(max_length=55,null=True)
    account_email = models.CharField(max_length=55,null=True)
    business_name = models.CharField(max_length=55,null=True)
    business_type = models.CharField(choices=business_type,null=True,max_length=25)
    branh_ifsc_code = models.CharField(max_length=25,null=True)
    account_no = models.CharField(max_length=25,null=True)
    re_account_no = models.CharField(max_length=25,null=True)
    beneficiary_name = models.CharField(max_length=25,null=True)
    account_verifly_status = models.BooleanField(default=False)
    company_id = models.ForeignKey(company_Master,related_name='Bank_account_master_company_id',null=True,on_delete=models.CASCADE)
    account_id = models.CharField(max_length=55,null=True)


notification_type = (
     ("Bank Account","Bank Account"),
   
)
class notification(common):
    notification_type = models.CharField(choices=notification_type,null=True,max_length=25)
    mapping_id = models.IntegerField(null=True)
    read_status = models.BooleanField(default=False)
    company_id = models.ForeignKey(company_Master,related_name='notification_id',null=True,on_delete=models.CASCADE)
    

class Event_Booking_Table(common):
    event_id = models.ForeignKey(event_Creation,related_name='Event_Booking_Table_event_id',null=True,on_delete=models.CASCADE)
    order_id = models.CharField(max_length=55,null=True)
    payment_id = models.CharField(max_length=55,null=True)
    total_paid_amount = models.FloatField(null=True)
    received_amount = models.FloatField(null=True)
    payment_status = models.BooleanField(default=False)

class Event_Booking_user_Data(common):
    event_id = models.ForeignKey(event_Creation,related_name='Event_Booking_user_Data_bookig_table_id',null=True,on_delete=models.CASCADE)
    event_creation_id = models.ForeignKey(Event_Booking_Table,related_name='Event_Booking_user_Data_event_id',null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=25,null=True)
    email = models.CharField(max_length=25,null=True)
    phone = models.CharField(max_length=25,null=True)
    ticket_type_id = models.ForeignKey(Event_ticket,related_name='Event_Booking_user_Data_ticket_type_id',null=True,on_delete=models.CASCADE)
    ticket_confirm_status = models.BooleanField(default=False)


class Event_booking_user_question_table(common):
    event_user_id = models.ForeignKey(Event_Booking_user_Data,related_name='Event_booking_user_question_table_user_id',null=True,on_delete=models.CASCADE)
    question_id = models.ForeignKey(Event_question,related_name='Event_booking_user_question_table_question_id',null=True,on_delete=models.CASCADE)
    answer = models.CharField(max_length=255,null=True)
    