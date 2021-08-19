from django.contrib import admin

# Register your models here.
from .models import Students,Login

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','username')
class LoginAdmin(admin.ModelAdmin):
    list_display = ('username','type')


admin.site.register(Students,StudentAdmin)
admin.site.register(Login,LoginAdmin)







