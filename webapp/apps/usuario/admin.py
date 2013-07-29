from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from models import  UserProfile




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
    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)





class  UserProfileAdmin(admin.ModelAdmin):

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


#admin.site.unregister(Site)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile,UserProfileAdmin)

