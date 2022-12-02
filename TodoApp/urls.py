from . import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    path('detailedview/<int:pk>/',views.Taskdetailedview.as_view(),name='detailedview'),
    path('taskupdate/<int:pk>/',views.Taskupdateview.as_view(),name='taskupdate'),
    path('taskdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='taskdelete'),
]
