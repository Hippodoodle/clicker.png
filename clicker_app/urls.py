from django.urls import path
from clicker_app import views

app_name = 'clicker_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('logout/', views.logout_view, name='logout'),
    path('add_points/', views.AddPoints.as_view(), name='add_points'),
]
