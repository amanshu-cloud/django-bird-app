from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Post
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'age', 'name', 'gender', 'country', 'email', 'password']
    fieldsets = (
        (('User'), {'fields': ('username', 'age', 'name', 'gender', 'country', 'email', 'password')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post)