from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('all/', views.user_list_view, name='index'),
    path('<int:user_id>/', views.user_detail_view, name='detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]