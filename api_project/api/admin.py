from django.contrib import admin
from .models import Book

<<<<<<< HEAD
# Register your models here.


admin.site.register(Book)
=======

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', )
    list_filter = ('title', 'author', )


admin.site.register(Book,BookAdmin)  
 
>>>>>>> 4426c1bee6525b3a7279a2554af64684bd8720bd
