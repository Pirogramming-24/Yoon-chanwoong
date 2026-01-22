# user/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # 관리자 목록 화면에서 보여줄 필드들
    list_display = ('username','password')