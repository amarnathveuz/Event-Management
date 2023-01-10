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
    return render(request,'category.html')



def create_category(request):
    return render(request,'create_category.html')


def event(request):
    return render(request,'event.html')


def create_event(request):
    return render(request,'create_event.html')



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

    