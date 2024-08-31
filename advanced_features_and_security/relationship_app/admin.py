from django.contrib import admin

# Register your models here.

from.models import user
from django.contrib.auth.admin import UserAdmin

class customer_admin(UserAdmin):
    list_display = ('username','email','first_name','last_name','is_staff','is_active')
    search_fields =("email","username","last_name")
    list_filter = ("is_staff","is_active")
    fieldsets = ()
    add_fieldsets = ()
    filter_horizontal = ()

    

admin.site.register(user,customer_admin)




