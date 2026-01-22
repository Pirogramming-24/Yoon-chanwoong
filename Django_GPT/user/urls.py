from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('<int:pk>/', views.login, name='login'),
    path('logout/',views.logout_fun,name="logout"),
    path('signup/',views.signup,name="signup")
]