from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile
from maintenance.admin import WorkerInline

# Reference: https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html
# This class is our profile class
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'  # since only a profile is associated with a User model, its plural name will besame
    fk_name = 'user'  # This is the OneToOne field in the Profile model


# This shows our associated profile with the User model, together with the user model edit form in the admin
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, WorkerInline, )
    list_display = ('username', 'first_name', 'is_staff', 'get_user_type')
    list_select_related = ('profile', 'worker', )  # To reduce many queries to the database

    def get_user_type(self, instance):
        return str(instance.profile.user_type)
    get_user_type.short_description = 'User Type'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
