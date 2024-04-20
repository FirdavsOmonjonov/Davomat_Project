from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    #-----------Login--------------------
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='log_out'),
    #-----------Errorlar--------------------
    path('error1/',views.error1,name='error1'),
    path('error2/',views.error2,name='error2'),
]