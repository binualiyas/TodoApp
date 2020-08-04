from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('home', views.home, name='home'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('delete', views.deleteComplete, name='delete'),
    path('deleteall', views.deleteAll, name='deleteall'),
    path('dashboard/', views.dashboardView,name='dashboard'),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',views.registerView,name='register'),
    path('logout/',LogoutView.as_view(next_page='index'),name='logout'), 
]