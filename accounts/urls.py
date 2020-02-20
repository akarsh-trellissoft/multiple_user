from django.urls import path,include
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('user',views.user,name='user'),
    path('admin',views.admin,name='admin'),

]
