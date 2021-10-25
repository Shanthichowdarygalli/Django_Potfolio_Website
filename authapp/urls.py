from django.urls import path
from . import views

urlpatterns = [
    path('user_reg/', views.user_registration, name='user_reg'),# http://127.0.0.1:8000/authapp/user_reg/
    path('profile/', views.user_profile, name='profile'),# http://127.0.0.1:8000/authapp/profile/
    path('login/', views.user_login, name='login'),# http://127.0.0.1:8000/authapp/login/
    path('logout/', views.user_logout, name='logout'),# http://127.0.0.1:8000/authapp/logout/

    path('add_profile_pic/', views.add_profile_pic, name='add_profile_pic'),  # http://127.0.0.1:8000/authapp/logout/
    path('update_profile_pic/', views.update_profile_pic, name='update_profile_pic'),
    # http://127.0.0.1:8000/authapp/logout/

]


