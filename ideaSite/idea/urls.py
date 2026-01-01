from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_page,name='main'),
    path('detail/',views.detail_page,name='detail'),
    path('modify/',views.modify_page,name='modify'),
    path('register/',views.register_page,name='register'),
    path('tool_detail/',views.tool_detail_page,name='tool_detail'),
    path('tool_manage/',views.tool_manage_page,name='tool_manage'),
    path('tool_modify/',views.tool_modify_page,name='tool_modify'),
    path('tool_register/',views.tool_register_page,name='tool_register')
]