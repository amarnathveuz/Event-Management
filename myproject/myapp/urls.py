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
    path('test_r1',views.test_r1,name='test_r1'),
    path('event_attendees_user_modal',views.event_attendees_user_modal,name='event_attendees_user_modal'),
    path('confirm_booking_action',views.confirm_booking_action,name='confirm_booking_action'),
    path('attend_booking_action',views.attend_booking_action,name='attend_booking_action'),
    path('cancel_booking_action',views.cancel_booking_action,name='cancel_booking_action'),
    path('configuration',views.configuration,name='configuration'),
    path('sponsor_level',views.sponsor_level,name='sponsor_level'),
    path('create_sponsor_level',views.create_sponsor_level,name='create_sponsor_level'),
    path('edit_sponsor_level/<int:pk>',views.edit_sponsor_level,name='edit_sponsor_level'),
    path('sponsor_type',views.sponsor_type,name='sponsor_type'),
    path('create_sponsor_type',views.create_sponsor_type,name='create_sponsor_type'),
    path('edit_sponsor_type/<int:pk>',views.edit_sponsor_type,name='edit_sponsor_type'),
    path('booth_category',views.booth_category,name='booth_category'),
    path('create_booth',views.create_booth,name='create_booth'),
    path('edit__booth_category/<int:pk>',views.edit__booth_category,name='edit__booth_category'),
    path('event_create_booth/<int:pk>',views.event_create_booth,name='event_create_booth'),
    path('create_event_booth/<int:pk>',views.create_event_booth,name='create_event_booth'),









    
    
    
    
    
    

    
    




]