from django.contrib import admin
from .models import CustomUser,Book,Transaction,LibraryUser


class admin_model (admin.ModelAdmin):
    list_display = ('username', 'email',)

class Book_admin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'number_of_copies')   
   
class librayuser_Admin(admin.ModelAdmin):
    list_display = ('date_of_membership','is_active')
   





# Register your models here.

admin.site.register(Book,Book_admin)
admin.site.register(Transaction)
admin.site.register(CustomUser,admin_model)

admin.site.register(LibraryUser,librayuser_Admin)
