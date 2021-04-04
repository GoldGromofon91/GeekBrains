from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('user/register/',authapp.register_user, name='register'),
    path('user/edit/',authapp.profile_edit, name='profile_edit'),
    path('user/verify/<str:email>/<str:activation_key>',authapp.verify_user, name='verify_user')
]