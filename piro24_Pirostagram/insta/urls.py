from . import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'insta'

urlpatterns = [
    path('',views.mainPage,name="mainPage"),
    path('profile/<int:pk>/',views.profile,name="profile"),
    path('follow/<int:pk>/',views.follow,name="follow"),
    path('makepost/',views.makepost,name="makepost"),
    path('modify/<int:pk>',views.modify,name="modify"),
    path('post/like/', views.post_like_ajax, name='post_like_ajax'),
    path('story/', views.makestory, name='makestory'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)