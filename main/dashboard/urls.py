from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index , name='index'),
    #-------Profile--------------------
    path('profile-edit', views.profile_edit, name='profile_edit'),
    path('update-password,', views.update_password, name='update_password'),
    # ------Xodimlar--------------------
    path('staff-create', views.staff_create, name='staff_create'),
    path('staff-list', views.staff_list, name='staff_list'),
    path('staff-detail/<int:id>/', views.staff_detail, name='staff_detail'),
    path('staff-delete/<int:id>/', views.staff_delete, name='staff_delete'),
    path('staff-update/<int:id>/', views.staff_update, name= 'staff_update'),
    # ------Davomat---------------------
    path('attendance-list', views.attendance_list, name='attendance_list'),  
]