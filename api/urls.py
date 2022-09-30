from django.urls import path
from . import views

urlpatterns = [
    # path('',views.apiOverview,name='apiview'),
    path('',views.StudentList,name='stu_list'),
    path('studentdetail/<str:pk>',views.StudentDetail,name='stu_detail'),
    path('studentcreate',views.StudentCreate,name='stu_create'),
    path('studentupdate/<str:pk>',views.StudentUpdate,name='stu_update'),
    path('studentdelete/<str:pk>',views.StudentDelete,name='stu_delete'),
]
