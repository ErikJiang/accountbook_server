from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from apps.users.forms import CustomUserCreationForm, CustomUserChangeForm
from apps.users.models import CustomUser

class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  model = CustomUser
  list_display = ['email', 'username', 'name']

admin.site.register(CustomUser, CustomUserAdmin)
