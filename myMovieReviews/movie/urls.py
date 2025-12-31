from django.urls import path
from . import views
urlpatterns = [
    path('',views.review_lists, name='review_lists'),
    path('detail/',views.review_detail, name='review_detail'),
    path('write/',views.review_write, name='review_write'),
    path('modify/<int:pk>', views.review_modify,name='review_modify')
]