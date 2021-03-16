from django.urls import re_path
from LoginApp import views

app_name = 'LoginApp'

urlpatterns = [

    #re_path(r'^register',views.registration,name = 'registration'),
    re_path(r'^register/',views.register,name = 'register'),
    re_path(r'^user_login/$',views.user_login,name = 'user_login'),
]
