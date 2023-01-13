from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.authtoken.models import Token
from .models import *
from django.db import IntegrityError, transaction

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
        ticket_instructions = request.POST.getlist("ticket_instructions")
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
    context = {
        'data':data,
        'data_event_note':data_event_note
    }
    return render(request,'event_more_page.html',context)


def event_website(request):
    slug = request.GET.get("slug")
    print("slug::::",str(slug))
    data = event_Creation.objects.get(slug=slug)
    context = {
        'data':data
    }
    return render(request,'event_website.html',context)



def dynamic_url(request,id):
    
    pass