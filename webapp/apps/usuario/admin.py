from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.models import Site
from django.contrib.auth.models import User

from usuario.models import  UserProfile




# Adding UserProfile fields to the admin
# Define an inline admin descriptor for User model
# which acts a bit like a singleton
class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Usuarios'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserInline, )
    list_display = ('username',  'is_active', 'date_joined', 'is_staff')
#    fieldsets = (
#        (None, {'fields': ('username', 'password')}),
#        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
#    )


class UserProfileCreationForm(UserCreationForm):
    """
    A form that overrides the UserCreationForm
    """
    class Meta:
        model = User
        fields = ("username", "groups")

UserAdmin.add_form = UserProfileCreationForm

admin.site.unregister(Site)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)

