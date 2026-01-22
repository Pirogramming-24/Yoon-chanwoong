from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('',views.login_to,name='login_to'),
    path('<int:pk>/', views.login, name='login'),
    path('logout/',views.logout_fun,name="logout"),
    path('signup/',views.signup,name="signup")
]