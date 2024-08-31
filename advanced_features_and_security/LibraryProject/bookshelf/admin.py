from django.contrib import admin

# Register your models here.
from .models import Book

from django.contrib import admin

# Register your models here.

from.models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# first is the user custom model

class CustomUserAdmin(UserAdmin):
    list_display = ('username','email','first_name','last_name','is_staff','is_active')
    search_fields =("email","username","last_name")
  
 

admin.site.register( CustomUser, CustomUserAdmin)










# books class 
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    
    search_fields = ('title', 'author')


admin.site.register(Book,BookAdmin)

