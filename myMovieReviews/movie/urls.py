from django.urls import path
from . import views
urlpatterns = [
    path('',views.review_lists, name='review_lists'),
    path('detail/',views.review_detail, name='review_detail'),
    path('edit/',views.review_write_modify, name='review_write_modify'),
]