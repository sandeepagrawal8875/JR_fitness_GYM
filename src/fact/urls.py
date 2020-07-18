from django.urls import path
from . import views

urlpatterns = [
    # Root
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('calculate_BMI/', views.calculate_BMI, name='calculate_BMI'),

    # Blog
    path('blog/', views.blog, name='blog'),
    path('blog/<int:blog_id>', views.blog_details, name='blog_details'),
    path('delete_blog/<str:pk>/', views.delete_blog, name='delete_blog'),

    # Trainer
    path('trainer/', views.trainer, name='trainer'),
    path('trainer_form/<int:pk>/', views.update_trainer, name='trainer_form'),
    path('delete_trainer/<str:pk>/', views.delete_trainer, name='delete_trainer'),

    # Equipment
    path('equipment_galary/', views.equipment_galary, name='equipment_galary'),
    path('delete/<str:pk>/', views.delete_equp, name='delete_equp'),

    # achievement
    path('achivements/', views.achivements, name='achivements'),
    path('delete_achi/<str:pk>/', views.delete_achi, name='delete_achi'),

    # login
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logout_User, name="logout"),

    # Admin
    path('admin_page/', views.owner_admin, name='admin_page'),

    # Client
    path('client/', views.client, name='client'),
    path('delete_client/<str:pk>/', views.delete_client, name='delete_client'),
    path('update_client/<int:pk>/', views.update_client, name='update_client'),

    # Staff
    path('staff/', views.staff, name='staff'),
    path('delete_staff/<str:pk>/', views.delete_staff, name='delete_staff'),
    path('update_staff/<int:pk>/', views.update_staff, name='update_staff'),

    # Visitor
    path('visitor/', views.visitor, name='visitor'),
    path('delete_visitor/<str:pk>/', views.delete_visitor, name='delete_visitor'),

]
