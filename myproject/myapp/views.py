from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.authtoken.models import Token
from .models import *
from django.db import IntegrityError, transaction
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

# Create your views here.


def index(request):
    return render(request,'index.html')


def dashboard(request):
    return render(request,'dashboard.html')


def company_user(request):
    auth_user = User.objects.get(id=request.user.id)
    if auth_user.is_superuser == True:
        data = company_User.objects.all().order_by('-id')
    else:
        user_data = company_User.objects.get(auth_user=request.user)

        data = company_User.objects.filter(company_id_id=user_data.company_id.id,user_type="company_staff")
    context = {
        'data':data
    }
    return render(request,'company_user.html',context)


def create_company_user(request):

    auth_user = User.objects.get(id=request.user.id)
    if auth_user.is_superuser == True:

        return render(request,'create_company_user.html')
    else:
        data_user = company_User.objects.get(auth_user=request.user)
        return render(request,'create_company_user.html',{'data_user':data_user})


def role_management(request):
    auth_user_data = User.objects.get(id=request.user.id)
    if auth_user_data.is_superuser == True:
        data = ''
    else:
        user_model = company_User.objects.get(auth_user=request.user)

        data = company_Role_Master.objects.filter(company_id=user_model.company_id)
    context = {
        'data':data
    }
    return render(request,'role_management.html',context)


def create_role(request):
    if request.method == "POST":
        try:
                with transaction.atomic():
                    Name = request.POST.get("Name",False)
                    description = request.POST.get("description",False)
                    user_data = company_User.objects.get(auth_user=request.user)
                    data_role = company_Role_Master.objects.create(role_name=Name,description=description,company_id=user_data.company_id,created_by=request.user)
                    data_user_management = company_Role_Nav_Master.objects.create(
                        role_id_id =  data_role.id,
                        nav_name = "User Management",
                        Read = request.POST.get("user_management_read",False),
                        Write = request.POST.get("user_management_write",False),
                        Edit = request.POST.get("user_management_edit",False),
                        Delete = request.POST.get("user_management_delete",False),
                        View_All = request.POST.get("user_management_view_all",False),
                        Manage_All = request.POST.get("user_management_manage_all",False),
                    )
                    data_role_management = company_Role_Nav_Master.objects.create(
                        role_id_id =  data_role.id,
                        nav_name = "Role Management",
                        Read = request.POST.get("Role_management_read",False),
                        Write = request.POST.get("Role_management_write",False),
                        Edit = request.POST.get("Role_management_edit",False),
                        Delete = request.POST.get("Role_management_delete",False),
                        View_All = request.POST.get("Role_management_view_all",False),
                        Manage_All = request.POST.get("Role_management_manage_all",False),
                    )
                    data_Category_management = company_Role_Nav_Master.objects.create(
                        role_id_id =  data_role.id,
                        nav_name = "Category Management",
                        Read = request.POST.get("Category_management_read",False),
                        Write = request.POST.get("Category_management_write",False),
                        Edit = request.POST.get("Category_management_edit",False),
                        Delete = request.POST.get("Category_management_delete",False),
                        View_All = request.POST.get("Category_management_view_all",False),
                        Manage_All = request.POST.get("Category_management_manage_all",False),
                    )
                    data_Event_management = company_Role_Nav_Master.objects.create(
                        role_id_id =  data_role.id,
                        nav_name = "Event Management",
                        Read = request.POST.get("Event_management_read",False),
                        Write = request.POST.get("Event_management_write",False),
                        Edit = request.POST.get("Event_management_edit",False),
                        Delete = request.POST.get("Event_management_delete",False),
                        View_All = request.POST.get("Event_management_view_all",False),
                        Manage_All = request.POST.get("Event_management_manage_all",False),
                    )
                    data_Booking_management = company_Role_Nav_Master.objects.create(
                        role_id_id =  data_role.id,
                        nav_name = "Booking Management",
                        Read = request.POST.get("Booking_management_read",False),
                        Write = request.POST.get("Booking_management_write",False),
                        Edit = request.POST.get("Booking_management_edit",False),
                        Delete = request.POST.get("Booking_management_delete",False),
                        View_All = request.POST.get("Booking_management_view_all",False),
                        Manage_All = request.POST.get("Booking_management_manage_all",False),
                    )
                    data_Notification_management = company_Role_Nav_Master.objects.create(
                        role_id_id =  data_role.id,
                        nav_name = "Notification",
                        Read = request.POST.get("Notification_management_read",False),
                        Write = request.POST.get("Notification_management_write",False),
                        Edit = request.POST.get("Notification_management_edit",False),
                        Delete = request.POST.get("Notification_management_delete",False),
                        View_All = request.POST.get("Notification_management_view_all",False),
                        Manage_All = request.POST.get("Notification_management_manage_all",False),
                    )
                    messages.success(request,'role successfully created')
                    return redirect(request.META['HTTP_REFERER'])
        except:
            pass
        
    return render(request,'create_role.html')


def category(request):

    auth_user  = User.objects.get(id=request.user.id)
    if auth_user.is_superuser == True:
        data = ''
    else:
        user_data = company_User.objects.get(auth_user=request.user)
        company_id = user_data.company_id.id
        data = event_Category.objects.filter(company_id_id=company_id)
    context = {
        'data':data
    }
    return render(request,'category.html',context)



def create_category(request):
    if request.method == "POST":
        auth_user = User.objects.get(id=request.user.id)
        if auth_user.is_superuser == True:
            pass
        else:
            category_name = request.POST.get("category_name",False)
            description = request.POST.get("description",False)
            user_data = company_User.objects.get(auth_user=request.user)
            company_id = user_data.company_id
            data_save_cat  = event_Category.objects.create(category_name=category_name,company_id_id=company_id.id,description=description,created_by=request.user)
            messages.success(request,'event category successfully created')
            return redirect(request.META['HTTP_REFERER'])
            
    return render(request,'create_category.html')


def event(request):
    auth_user = User.objects.get(id=request.user.id)
    print("auth_user::::",str(auth_user.is_superuser))
    if auth_user.is_superuser == True:
        data = ''
    else:
        user_data = company_User.objects.get(auth_user=request.user)
        
        data = event_Creation.objects.filter(company_id_id=user_data.company_id.id)
    context = {
        'data':data
    }
    return render(request,'event.html',context)


def create_event(request):
    if request.method == "POST":
        # auth_user = User.objects.get(id=request.user.id)
        user_data = company_User.objects.get(auth_user=request.user)
        name = request.POST.get("name")
        start_date = request.POST.get("start_date")
        start_time = request.POST.get("start_time")
        end_date = request.POST.get("end_date")
        end_time = request.POST.get("end_time")
        image = request.FILES['image']
        organizer = request.POST.get("organizer")
        responsible = request.POST.get("responsible")
        responsible_person_no = request.POST.get("responsible_person_no")
        company = request.POST.get("company")
        venue = request.POST.get("venue")
        exhibition_map = request.POST.get("exhibition_map")
        limit_registrations = request.POST.get("limit_registrations")
        if limit_registrations == None:
            limit_registrations = False
        limit_registration_no = request.POST.get("limit_registration_no")
        if limit_registration_no == '':
            limit_registration_no = 0
        category_id = request.POST.get("category_id")
        ticket_name = request.POST.getlist("ticket_name[]")
        ticket_description = request.POST.getlist("ticket_description[]")
        ticket_product = request.POST.getlist("ticket_product[]")
        ticket_price = request.POST.getlist("ticket_price[]")
        ticket_salestart = request.POST.getlist("ticket_salestart[]")
        ticket_saleend = request.POST.getlist("ticket_saleend[]")
        ticket_maximum = request.POST.getlist("ticket_maximum[]")
        data_save_event = event_Creation.objects.create(name=name,start_date=start_date,start_time=start_time,end_date=end_date,end_time=end_time,image=image,organizer=organizer,responsible=responsible,responsible_person_no=responsible_person_no,company=company,company_id_id=user_data.company_id.id,venue=venue,limit_registrations=limit_registrations,limit_registration_no=limit_registration_no,category_id_id=category_id,created_by=request.user)
        ticket_zip_object = zip(ticket_name,ticket_description,ticket_product,ticket_price,ticket_salestart,ticket_saleend,ticket_maximum)
        for name,description,product,price,salestart,saleend,maximum in ticket_zip_object:
            data_save_Event_ticket = Event_ticket(
                event_id_id = data_save_event.id,
                name = name,
                description = description,
                product  = product,
                price = price,
                sale_start_dt = salestart,
                sale_end_dt = saleend,
                maximum = maximum

            )
            data_save_Event_ticket.save()
        question_title = request.POST.getlist("question_title[]")
        question_type = request.POST.getlist("question_type[]")
        questionanswercount = request.POST.getlist("questionanswercount[]")
        question_zip_object = zip(question_title,question_type,questionanswercount)
        for title,type,answer_count in question_zip_object:
            save_Event_question = Event_question.objects.create(event_id_id=data_save_event.id,question_type=type,title=title)
            if type == "Selection":
                select_name = request.POST.getlist("select_name"+answer_count+"[]")
                for i in select_name:
                    save_select_answer = Event_selection_question.objects.create(Event_question_id_id=save_Event_question.id,answer=i)
        note = request.POST.get("note")
        ticket_instructions = request.POST.get("ticket_instructions")
        save_note = Event_note.objects.create(event_id_id=data_save_event.id,note=note,ticket_instructions=ticket_instructions)
        
        messages.success(request,'event  successfully created')
        return redirect(request.META['HTTP_REFERER'])
    
    user_auth = User.objects.get(id=request.user.id)
    if user_auth.is_superuser == True:
        data = ''
    else:
        user_data = company_User.objects.get(auth_user=request.user)
        data = event_Category.objects.filter(company_id_id=user_data.company_id.id)
    context = {
        'data':data
    }
    return render(request,'create_event.html',context)



def login_action(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = authenticate(username=username, password=password)
            st = user.is_superuser
            if st == True:
                login(request, user)
                return redirect('dashboard')
            else:
                login(request, user)
                return redirect('dashboard')
        except:
            messages.warning(request,"invalid username and password")
            return redirect(request.META['HTTP_REFERER'])



def create_company_action(request):
    if request.method == "POST":
        company_name = request.POST.get("company_name")
        name = request.POST.get("name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password_option = request.POST.get("password_option")
        phone = request.POST.get("phone")
        photo = request.FILES['photo']
        if password_option == "Automatic":
            import string    
            import random
            S = 10
            password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
        elif password_option == "Manual":

            password = request.POST.get("password",False)

        if User.objects.filter(username=username).exists():
                messages.warning(request,str("An account with the given username already exists"))
                return redirect(request.META['HTTP_REFERER'])
        else:
            try:
                with transaction.atomic():
                    user = User.objects.create_user(username, email, password)
                    user.save()
                    data1 = Token.objects.create(user=user)

                    auth_user_model = User.objects.get(id=request.user.id)
                    if auth_user_model.is_superuser == True:
                        data_save_company = company_Master.objects.create(company_name=company_name,auth_user_id=user)
                        company_id = data_save_company.id 
                        user_type = "company_admin"
                    else:
                        user_data = company_User.objects.get(auth_user_id=request.user.id)
                        company_id = user_data.company_id.id 
                        company_name = user_data.company_id.company_name 
                        user_type = "company_staff"


                    
                    save_company_model =  company_User(
                        auth_user  = user,
                        company_name = company_name,
                        name = name,
                        username = username,
                        email = email,
                        password_option = password_option,
                        phone = phone,
                        photo = photo,
                        user_type = user_type,
                        created_by = request.user,
                        company_id_id = company_id

                    )
                    save_company_model.save()
                    messages.success(request,'account successfully created')
                    return redirect(request.META['HTTP_REFERER'])
            except IntegrityError:
                pass
            pass
        

def edit_user(request,pk):
    if request.method == "POST":
        id = request.POST.get("id")
        company_name = request.POST.get("company_name")
        name = request.POST.get("name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password_option = request.POST.get("password_option")
        phone = request.POST.get("phone")
        change_profile_pic = request.POST.get("change_profile_pic")
        user_data = company_User.objects.get(id=id)
        if password_option == "Yes":
            password = request.POST.get("password")
            u = User.objects.get(id=user_data.auth_user.id)
            u.set_password(password)
            u.save()
        if change_profile_pic == "Yes":
            update_user_data = company_User.objects.get(id=id)
            photo = request.FILES['photo']
            update_user_data.photo = photo
            update_user_data.save()
        update_company = company_User.objects.filter(id=id).update(company_name=company_name,name=name,email=email,phone=phone)
        messages.success(request,'account successfully updated')
        return redirect(request.META['HTTP_REFERER'])
    else:
        data = company_User.objects.get(id=pk)
        context = {
            'data':data
        }
        return render(request,'edit_user.html',context)



def edit_role(request,pk):

    if request.method == "POST":
        id = request.POST.get("id")
        Name = request.POST.get("Name")
        description = request.POST.get("description")
        data_update = company_Role_Master.objects.filter(id=id).update(role_name=Name,description=description)
        data_user_management = company_Role_Nav_Master.objects.filter(role_id_id =id,nav_name = "User Management").update(
                        
                        
                        Read = request.POST.get("user_management_read",False),
                        Write = request.POST.get("user_management_write",False),
                        Edit = request.POST.get("user_management_edit",False),
                        Delete = request.POST.get("user_management_delete",False),
                        View_All = request.POST.get("user_management_view_all",False),
                        Manage_All = request.POST.get("user_management_manage_all",False),
        )
        data_role_management = company_Role_Nav_Master.objects.filter(role_id_id=id,  nav_name = "Role Management").update(
                       
                      
                        Read = request.POST.get("Role_management_read",False),
                        Write = request.POST.get("Role_management_write",False),
                        Edit = request.POST.get("Role_management_edit",False),
                        Delete = request.POST.get("Role_management_delete",False),
                        View_All = request.POST.get("Role_management_view_all",False),
                        Manage_All = request.POST.get("Role_management_manage_all",False),
        )
        data_Category_management = company_Role_Nav_Master.objects.filter(role_id_id=id,nav_name = "Category Management").update(
                       
                        
                        Read = request.POST.get("Category_management_read",False),
                        Write = request.POST.get("Category_management_write",False),
                        Edit = request.POST.get("Category_management_edit",False),
                        Delete = request.POST.get("Category_management_delete",False),
                        View_All = request.POST.get("Category_management_view_all",False),
                        Manage_All = request.POST.get("Category_management_manage_all",False),
        )
        data_Event_management = company_Role_Nav_Master.objects.filter(role_id_id=id, nav_name = "Event Management").update(
                        
                       
                        Read = request.POST.get("Event_management_read",False),
                        Write = request.POST.get("Event_management_write",False),
                        Edit = request.POST.get("Event_management_edit",False),
                        Delete = request.POST.get("Event_management_delete",False),
                        View_All = request.POST.get("Event_management_view_all",False),
                        Manage_All = request.POST.get("Event_management_manage_all",False),
        )
        data_Booking_management = company_Role_Nav_Master.objects.filter(role_id_id=id,nav_name = "Booking Management").update(
                     
                        
                        Read = request.POST.get("Booking_management_read",False),
                        Write = request.POST.get("Booking_management_write",False),
                        Edit = request.POST.get("Booking_management_edit",False),
                        Delete = request.POST.get("Booking_management_delete",False),
                        View_All = request.POST.get("Booking_management_view_all",False),
                        Manage_All = request.POST.get("Booking_management_manage_all",False),
        )
        data_Notification_management = company_Role_Nav_Master.objects.filter(role_id_id=id,nav_name = "Notification").update(
                       
                        Read = request.POST.get("Notification_management_read",False),
                        Write = request.POST.get("Notification_management_write",False),
                        Edit = request.POST.get("Notification_management_edit",False),
                        Delete = request.POST.get("Notification_management_delete",False),
                        View_All = request.POST.get("Notification_management_view_all",False),
                        Manage_All = request.POST.get("Notification_management_manage_all",False),
        )
        messages.success(request,'role successfully updated')
        return redirect(request.META['HTTP_REFERER'])

    role_data = company_Role_Master.objects.get(id=pk)

    role_user_management = company_Role_Nav_Master.objects.get(role_id_id=pk,nav_name="User Management")
    role_Role_management = company_Role_Nav_Master.objects.get(role_id_id=pk,nav_name="Role Management")
    role_Category_management = company_Role_Nav_Master.objects.get(role_id_id=pk,nav_name="Category Management")
    role_event_management = company_Role_Nav_Master.objects.get(role_id_id=pk,nav_name="Event Management")
    role_Booking_management = company_Role_Nav_Master.objects.get(role_id_id=pk,nav_name="Booking Management")
    role_Notification = company_Role_Nav_Master.objects.get(role_id_id=pk,nav_name="Notification")
    context = {
        'data':role_data,
        'role_user_management':role_user_management,
        'role_Role_management':role_Role_management,
        'role_Category_management':role_Category_management,
        'role_event_management':role_event_management,
        'role_Booking_management':role_Booking_management,
        'role_Notification':role_Notification
    }

    return render(request,'edit_role.html',context)

    


def edit_category(request,pk):
    if request.method == "POST":
        category_name= request.POST.get("category_name")
        id = request.POST.get("id")
        description = request.POST.get("description")
        update_category = event_Category.objects.filter(id=pk).update(category_name=category_name,description=description)
        messages.success(request,'event category successfully updated')
        return redirect(request.META['HTTP_REFERER'])

    data = event_Category.objects.get(id=pk)
    context = {
        'data':data
    }
    return render(request,'edit_category.html',context)



def event_more_page(request,pk):
    data = event_Creation.objects.get(id=pk)
    print("data::::",str(data))
    data_event_note = Event_note.objects.get(event_id_id=pk)
    booking_user_count = Event_Booking_user_Data.objects.filter(event_id=data.id,ticket_confirm_status=True).count()
    print("count:::",str(booking_user_count))
    context = {
        'data':data,
        'data_event_note':data_event_note,
        'booking_user_count':booking_user_count,
        'pk':pk
    }
    return render(request,'event_more_page.html',context)


def event_website(request):
    slug = request.GET.get("slug")
    print("slug::::",str(slug))
    data = event_Creation.objects.get(slug=slug)
    context = {
        'data':data,
        'slug':slug
    }
    return render(request,'event_website.html',context)


def test1(request):
    data = "amarnath"
    return redirect("http://"+data+".localhost:8000/")
    user_id = request.session['user_id']
    print("second::::::",str(user_id))
    return render(request,'hometest.html')



def dynamic_url(request):
    user_id = request.GET.get("user_id")
    print("user_id:::",str(user_id))
    print("first methoddd")
    request.session['user_id'] = user_id
    return redirect("test1")
    pass



def user_book_ticket(request):

    slug = request.GET.get("slug")
    select_data = request.GET.getlist("select_data[]")
    print("select_data::::",str(select_data))
    data2 = event_Creation.objects.get(slug=slug)
    data3 = Event_ticket.objects.filter(event_id_id=data2.id)

    event_question_data = Event_question.objects.filter(event_id_id=data2.id)
    return render(request,'user_book_ticket.html',{'data2':data3,'select_data':select_data,'event_id':data2.id,'event_question_data':event_question_data})
    

from collections import Counter
def book_data(request):
    if request.method == "POST":
        ticket_type_id = request.POST.getlist("ticket_type_id[]")
        ticket_dict = {}
        j = 0
        for i in ticket_type_id:
            ticket_dict["ticket_dict"+str(j)] = int(i)
            print(i)
            j = j+1
        res = Counter(ticket_dict.values())
        ticket_quantity = []
        total_paid_amount = 0
        for key, value in res.items():
            ticket_instance_modal = Event_ticket.objects.get(id=key)
            total_amount = ticket_instance_modal.price * value
            total_paid_amount +=total_amount
            a_dictionary = {"ticket_id" : key, "quantity" :value ,'total_amount':total_amount,'ticket_name':ticket_instance_modal.name}
            ticket_quantity.append(a_dictionary)
        name = request.POST.getlist("name[]")
        email = request.POST.getlist("email[]")
        phone = request.POST.getlist("phone[]")
        

        currency = 'INR'
        tax_per = int(total_paid_amount)/100*3
        total_paid_amount_data = total_paid_amount + tax_per
        amount = total_paid_amount_data * 100
        razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
        razorpay_order_id = razorpay_order['id']
        callback_url = 'paymenthandler/'
        context = {}
        context['ticket_quantity'] = ticket_quantity
        context['total_paid_amount'] =total_paid_amount
        context['tax_per'] = round(tax_per, 2)
        context['total_paid_amount_data'] = total_paid_amount_data
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['callback_url'] = callback_url
        context['name'] = name
        event_id = request.POST.get("event_id")
        zip_object = zip(name,email,phone,ticket_type_id)
        try:
            data = Event_Booking_Table.objects.get(order_id=razorpay_order_id)
        except:

            data_save = Event_Booking_Table.objects.create(event_id_id=event_id,order_id=razorpay_order_id,total_paid_amount=total_paid_amount_data,received_amount=total_paid_amount)
            i = 0
            ticket_type_id_count = request.POST.getlist("ticket_type_id_count[]")
            ticket_type_id_new = request.POST.getlist("ticket_type_id[]")
            for name,email,phone,ticket_type_id in zip_object:
                save_ticket = Event_Booking_user_Data.objects.create(event_id_id=event_id,event_creation_id_id=data_save.id,name=name,email=email,phone=phone,ticket_type_id_id=ticket_type_id)
                question_id = request.POST.getlist("question_id"+str(ticket_type_id_new[i]+str(ticket_type_id_count[i])+"[]"))
                question_answer = request.POST.getlist("question_answer"+str(ticket_type_id_new[i]+str(ticket_type_id_count[i]+"[]")))

                question_zip = zip(question_id,question_answer)
                for question_id,question_answer in question_zip:
                    data_save_question = Event_booking_user_question_table.objects.create(event_user_id_id=save_ticket.id,question_id_id=question_id,answer=question_answer)
                i = i + 1

        return render(request,'book_data.html',context)
        pass


def bank_account(request):
    bank_account = False
    user_data = company_User.objects.get(auth_user=request.user)
    data_bank = ''
    try:
        data_bank = Bank_account_master.objects.get(company_id_id=user_data.company_id.id)
        bank_account = True
    except:
        pass
    context = {
        'bank_account':bank_account,
        'data_bank':data_bank
    }
    return render(request,'bank_account.html',context)
    pass

def create_bank(request):
    if request.method == "POST":
        account_name = request.POST.get("account_name")
        account_email = request.POST.get("account_email")
        business_name = request.POST.get("business_name")
        business_type = request.POST.get("business_type")
        branh_ifsc_code = request.POST.get("branh_ifsc_code")
        account_no = request.POST.get("account_no")
        re_account_no = request.POST.get("re_account_no")
        beneficiary_name = request.POST.get("beneficiary_name")
        data_company = company_User.objects.get(auth_user=request.user)
        add_bank_account = Bank_account_master.objects.create(account_name=account_name,account_email=account_email,business_name=business_name,business_type=business_type,branh_ifsc_code=branh_ifsc_code,account_no=account_no,re_account_no=re_account_no,beneficiary_name=beneficiary_name,created_by=request.user,company_id_id=data_company.company_id.id)
        save_notification = notification.objects.create(notification_type="Bank Account",mapping_id=add_bank_account.id,company_id_id=data_company.company_id.id,created_by=request.user)
        return redirect("bank_account")

    return render(request,'create_bank.html')
    pass


def notifications(request):
    data = ''
    if request.user.is_superuser == True:
        data = notification.objects.filter(read_status=False)
    context = {
        'data':data
    }
    return render(request,'notifications.html',context)



def view_notification_more(request):
    mapping_id = request.GET.get("mapping_id")
    id = request.GET.get("id")
    print("mapping_id::::",str(mapping_id))
    data = Bank_account_master.objects.get(id=mapping_id)
    context = {
        'data':data,
        'notification_id':id
    }
    return render(request,'view_notification_more.html',context)


def verifly_account_action(request):
    if request.method == "POST":
        notification_id = request.POST.get("notification_id")
        update_id = request.POST.get("update_id")
        account_id = request.POST.get("account_id")
        update_notification = notification.objects.filter(id=notification_id).update(read_status=True)
        update_bank_account = Bank_account_master.objects.filter(id=update_id).update(account_verifly_status=True,account_id=account_id)
        return redirect("notifications")


import requests
import json


def razorpay_account_transfer_api(account_id,amount,name,payment_id):
    url = "https://api.razorpay.com/v1/payments/"+payment_id+"/transfers"
    payload = json.dumps({
        "transfers": [
        {
            "account": account_id,
            "amount": amount*100,
            "currency": "INR",
            "notes": {
                "name": name
            }
        }
        ]
    })
    headers = {
        'content-type': 'application/json',
        'Authorization': 'Basic cnpwX3Rlc3RfM3lFSUhKamVNRGpYcVU6UzE1M3JDZ09ZYU1KWlJnMUlST1VjVk9W'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

    pass






@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id', '')
        razorpay_order_id = request.POST.get('razorpay_order_id', '')
        signature = request.POST.get('razorpay_signature', '')
        params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
        }
        result = razorpay_client.utility.verify_payment_signature(
                params_dict)
        if result is not None:
            event_details_instance = Event_Booking_Table.objects.get(order_id=razorpay_order_id)
            user_company = event_details_instance.event_id.company_id
            amount = event_details_instance.total_paid_amount * 100
            data = razorpay_client.payment.capture(payment_id, amount)
            print("payment capture result---------")
            print(data)
            event_update = Event_Booking_Table.objects.filter(id=event_details_instance.id).update(payment_status=True,payment_id=payment_id)
            booking_update = Event_Booking_user_Data.objects.filter(event_creation_id_id=event_details_instance.id).update(ticket_confirm_status=True)
            print("user_company::::::::",str(user_company))
            data_account = Bank_account_master.objects.get(company_id_id=user_company)
            transfer_amount = razorpay_account_transfer_api(data_account.account_id,event_details_instance.received_amount,data_account.account_name,payment_id)
            return



def test_r1(request):
    return render(request,'test_r1.html')


def event_attendees_user_modal(request):
    id = request.GET.get("id")
    data = Event_Booking_user_Data.objects.filter(event_id_id=id,ticket_confirm_status=True)
    context = {
        'data':data
    }
    return render(request,'event_attendees_user_modal.html',context)




def confirm_booking_action(request):
    id = request.GET.get("id")
    print("id::::::::",str(id))
    data_update = Event_Booking_user_Data.objects.filter(id=id).update(confirm_status="confirm")
    messages.success(request,"Your booking has been confirmed")
    return redirect(request.META['HTTP_REFERER'])


def attend_booking_action(request):
    id = request.GET.get("id")
    print("id::::::::",str(id))
    data_update = Event_Booking_user_Data.objects.filter(id=id).update(confirm_status="attended")
    messages.success(request,"Attended")
    return redirect(request.META['HTTP_REFERER'])



def cancel_booking_action(request):
    id = request.GET.get("id")
    print("id::::::::",str(id))
    data_update = Event_Booking_user_Data.objects.filter(id=id).update(confirm_status="cancel")
    messages.success(request,"Your booking has been cancel")
    return redirect(request.META['HTTP_REFERER'])


def configuration(request):
    return render(request,'configuration.html')
    pass

def sponsor_level(request):
    user_data = company_User.objects.get(auth_user=request.user)
    company_id = user_data.company_id.id
    data = Sponsor_level.objects.filter(company_id_id=company_id)
    context = {
        'data':data
    }
    return render(request,'sponsor_level.html',context)


def create_sponsor_level(request):
    if request.method == "POST":
        sponsor_level = request.POST.get("sponsor_level")
        ribbon_style = request.POST.get("ribbon_style")
        user_data = company_User.objects.get(auth_user=request.user)
        company_id = user_data.company_id.id
        data_save = Sponsor_level.objects.create(company_id_id=company_id,sponsor_level=sponsor_level,ribbon_style=ribbon_style)
        messages.success(request,"success")
        return redirect(request.META['HTTP_REFERER'])
    return render(request,'create_sponsor_level.html')
    pass


def edit_sponsor_level(request,pk):

    if request.method == "POST":
        sponsor_level = request.POST.get("sponsor_level")
        ribbon_style = request.POST.get("ribbon_style")
        data_update = Sponsor_level.objects.filter(id=pk).update(sponsor_level=sponsor_level,ribbon_style=ribbon_style)
        messages.success(request,"update")
        return redirect(request.META['HTTP_REFERER'])
    data = Sponsor_level.objects.get(id=pk)
    context = {
        'data':data
    }
    
    return render(request,'edit_sponsor_level.html',context)



def sponsor_type(request):
    user_data = company_User.objects.get(auth_user=request.user)
    company_id = user_data.company_id.id
    data = Sponsor_Type.objects.filter(company_id_id=company_id)
    context = {
        'data':data
    }
    return render(request,'sponsor_type.html',context)



def create_sponsor_type(request):
    if request.method == "POST":
        user_data = company_User.objects.get(auth_user=request.user)
        company_id = user_data.company_id.id
        sponsor_type = request.POST.get("sponsor_type")
        data_save = Sponsor_Type.objects.create(company_id_id=company_id,sponsor_type=sponsor_type)
        messages.success(request,"success")
        return redirect(request.META['HTTP_REFERER'])

    return render(request,'create_sponsor_type.html')


def edit_sponsor_type(request,pk):
    if request.method == "POST":
        sponsor_type = request.POST.get("sponsor_type")
        data_update = Sponsor_Type.objects.filter(id=pk).update(sponsor_type=sponsor_type)
        messages.success(request,"update")
        return redirect(request.META['HTTP_REFERER'])
    data = Sponsor_Type.objects.get(id=pk)
    return render(request,'edit_sponsor_type.html',{'data':data})



def booth_category(request):
    user_data = company_User.objects.get(auth_user=request.user)
    company_id = user_data.company_id.id
    data = Booth_Category_type.objects.filter(company_id_id=company_id)
    context = {
        'data':data
    }
    return render(request,'booth_category.html',context)


def create_booth(request):
    if request.method == "POST":
        booth_category = request.POST.get("booth_category")
        product = request.POST.get("product")
        price = request.POST.get("price")
        sponser_status = request.POST.get("sponser_status")
        sponser_level = None
        sponsor_type = None
        sponser_status_new = False
        if sponser_status == 'on':
            sponser_level = request.POST.get("sponser_level")
            sponsor_type = request.POST.get("sponsor_type")
            sponser_status_new = True
        else:
            sponser_status_new = False
        user_data = company_User.objects.get(auth_user=request.user)
        company_id = user_data.company_id.id
        data_save = Booth_Category_type.objects.create(company_id_id=company_id,booth_category=booth_category,price=price,product=product,sponser_status=sponser_status_new,sponser_level_id=sponser_level,sponsor_type_id=sponsor_type)
        messages.success(request,"success")
        return redirect(request.META['HTTP_REFERER']) 
    user_data = company_User.objects.get(auth_user=request.user)
    company_id = user_data.company_id.id
    sponsor_level = Sponsor_level.objects.filter(company_id_id=company_id)
    sponsor_type = Sponsor_Type.objects.filter(company_id_id=company_id)
    context = {
        'sponsor_level':sponsor_level,
        'sponsor_type':sponsor_type
    }

    return render(request,'create_booth.html',context)



def edit__booth_category(request,pk):

    if request.method == "POST":
        booth_category = request.POST.get("booth_category")
        price = request.POST.get("price")
        sponser_status = request.POST.get("sponser_status")
        product = request.POST.get("product")
        if sponser_status == "on":
            sponser_level = request.POST.get("sponser_level")
            sponsor_type = request.POST.get("sponsor_type")
            update = Booth_Category_type.objects.filter(id=pk).update(booth_category=booth_category,price=price,product=product,sponser_status=True,sponser_level=sponser_level,sponsor_type=sponsor_type)
            pass
        else:
            update = Booth_Category_type.objects.filter(id=pk).update(booth_category=booth_category,price=price,product=product,sponser_status=False,sponser_level=None,sponsor_type=None)
            pass
        messages.success(request,"update")
        return redirect(request.META['HTTP_REFERER'])
    data = Booth_Category_type.objects.get(id=pk)
    user_data = company_User.objects.get(auth_user=request.user)
    company_id = user_data.company_id.id
    sponsor_level = Sponsor_level.objects.filter(company_id_id=company_id)
    sponsor_type = Sponsor_Type.objects.filter(company_id_id=company_id)
    context = {
        'data':data,
        'sponsor_level':sponsor_level,
        'sponsor_type':sponsor_type
    }
    return render(request,'edit__booth_category.html',context)


def event_create_booth(request,pk):
    context = {
        'pk':pk
    }
    return render(request,'event_create_booth.html',context)

    pass

def create_event_booth(request,pk):
    print("pk::::::::",str(pk))
    user_data = company_User.objects.get(auth_user=request.user)
    company_id = user_data.company_id.id
    booth_category = Booth_Category_type.objects.filter(company_id_id=company_id)
    context = {
        'booth_category':booth_category
    }
    return render(request,'create_event_booth.html',context)
    pass