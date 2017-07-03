from django.contrib import admin
from django.contrib.auth.models import User

from .models import Profile

# Register your models here.


class UserProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.UserAdmin):
    inline = [UserProfileInline]

admin.site.unregister(User)
admin.site.register((User, UserAdmin))
