from django.contrib import admin
from form.models import form 
# Register your models here.
class formAdmin(admin.ModelAdmin):
	list_display=('name','last_name','email','subject','msg')

admin.site.register(form,formAdmin)