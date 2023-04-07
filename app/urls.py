from django.urls import path
from . import views

urlpatterns=[
    path('', views.home_view, name='home'),
    # path('home/', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('appointment/', views.appointment_view, name='appointment'),
    path('contact/', views.customer_view, name='contact'),
    path('Login/', views.signin_view, name='signin'),
    path('logout/', views.signout, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('doctors/', views.doctors_view, name='doctors'),
    path('services/', views.services_view, name='services'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('viewcontact/', views.contact, name='contactview'),
    path('viewappointment/', views.appointment, name='appointmentview'),
    path('report/', views.view_report, name='report'),
    path('viewreport/', views.Report, name='reportview'),


]
