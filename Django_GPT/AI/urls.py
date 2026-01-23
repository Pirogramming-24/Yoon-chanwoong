from django.urls import path
from . import views

app_name='AI'

urlpatterns = [
    path('main/',views.main,name="main"),
    path('one/',views.AI_one_page,name="AI_one_page"),
    path('two/',views.AI_two_page,name="AI_two_page"),
    path('three/',views.AI_three_page,name="AI_three_page")
]