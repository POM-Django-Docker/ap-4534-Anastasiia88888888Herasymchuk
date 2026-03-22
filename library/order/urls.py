from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path("", views.order_list, name="index"),
    path("my/", views.order_list, name="my_orders"),
    path("all/", views.order_list, name="all_orders"),
    path("create/", views.order_create, name="create"),
    path("<int:pk>/", views.order_detail, name="detail"),
    path("<int:pk>/edit/", views.order_edit, name="edit"),
    path("<int:pk>/delete/", views.order_delete, name="delete"),
]
