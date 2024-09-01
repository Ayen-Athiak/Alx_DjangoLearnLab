from django.contrib import admin
#from.models import CustomUser
#from django.contrib.auth.admin import UserAdmin

from.models import Book

class admin_book(admin.ModelAdmin):
    list_display = ('title', 'author' )
    list_filter = ('title', 'author')

    search_fields = ('title', 'author')
    fieldsets = (
        (None, {
            'classes': ['wide'],
            'fields': ('username', 'password')
        }),
        ('Informations personnelles', {
            'classes': ['wide'],
            'fields': ('first_name', 'last_name', 'email', 'avatar')
        }),
        ('Permissions', {
            'classes': ['wide'],
            'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'permissions')
        }),
        ('Dates importantes', {
            'classes': ['wide'],
            'fields': ('last_login', 'date_joined')
        }),
    )


admin.site.register(Book,admin_book)





'''
class CustomUserAdmin(UserAdmin):
    list_display = ('username','email','first_name','last_name','is_staff','is_active')
    search_fields =("email","username","last_name")
  
 

admin.site.register(CustomUser, CustomUserAdmin)'''












