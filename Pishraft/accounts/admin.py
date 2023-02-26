from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.forms import UserCreationForm,UserChangeForm
from accounts.models import User, Otp_Code
from django.contrib.auth.models import Group
from django.contrib import auth


@admin.register(Otp_Code)
class OtpCodeAdmin(admin.ModelAdmin):
	list_display = ('phone_number', 'code', 'created')


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm 
    add_form = UserCreationForm

    list_display = ('full_name','phone_number','is_admin','id')
    list_filter = ('is_admin',)
    readonly_fields = ('last_login',)

    fieldsets = (
        ('main',{'fields':('phone_number','full_name','password','addresses','store_number','avatar')}),
        ('permission',{'fields':('is_active','is_admin','last_login',)})

    )

    add_fieldsets = (
        (None,{'fields':('phone_number','full_name','password1','last_login','is_admin','addresses','store_number','avatar')}),
    )

    search_fields = ('full_name',)
    ordering = ('full_name',)
    filter_horizontal = ()


admin.site.register(User,UserAdmin)
