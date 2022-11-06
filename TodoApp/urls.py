from . import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    path('/delete/<int:taskId>/',views.delete,name='delete'),
]