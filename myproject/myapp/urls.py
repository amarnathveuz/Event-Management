from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('company_user',views.company_user,name='company_user'),
    path('create_company_user',views.create_company_user,name='create_company_user'),
    path('role_management',views.role_management,name='role_management'),
    path('create_role',views.create_role,name='create_role'),
    path('category',views.category,name='category'),
    path('create_category',views.create_category,name='create_category'),
    path('event',views.event,name='event'),
    path('create_event',views.create_event,name='create_event'),
    path('login_action',views.login_action,name='login_action'),
    path('create_company_action',views.create_company_action,name='create_company_action'),
    path('edit_user/<int:pk>',views.edit_user,name='edit_user'),
    path('edit_role/<int:pk>',views.edit_role,name='edit_role'),
    path('edit_category/<int:pk>',views.edit_category,name='edit_category'),
    path('event_more_page/<int:pk>',views.event_more_page,name='event_more_page'),
    path('event_website',views.event_website,name='event_website'),
    path('r1',views.dynamic_url),
    path('test1',views.test1,name='test1'),
    path('user_book_ticket',views.user_book_ticket,name='user_book_ticket'),
    path('book_data',views.book_data,name='book_data'),
    path('bank_account',views.bank_account,name='bank_account'),
    path('create_bank',views.create_bank,name='create_bank'),
    path('notifications',views.notifications,name='notifications'),
    path('view_notification_more',views.view_notification_more,name='view_notification_more'),
    path('verifly_account_action',views.verifly_account_action,name='verifly_account_action'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('test_r1',views.test_r1,name='test_r1')
    
    
    
    
    
    

    
    




]