from django.urls import path
from . import views

app_name = 'teleapp'

urlpatterns = [
    path('', views.home, name='home'), # home url
    path('about/', views.about, name='about'), # about url
    path('contacts/', views.contacts, name='contacts'), # contacts url
    path('appointment/', views.appointment, name='appointment'), # appointment url
    path('services/', views.services, name='services'), # services url
    path('show_appointments/', views.fetch_appointments, name='show_appointments'), # show appointments url
    path('delete/<int:id>', views.delete_appointment, name='delete_appointment'),   # delete appointment url
    path('edit/<int:appointment_id>', views.update_appointment, name="update_appointment") # edit appointment url
]
