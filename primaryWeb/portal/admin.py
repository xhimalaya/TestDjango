from django.contrib import admin
from .models import *

class WebUsersAdmin(admin.ModelAdmin):
	list_display = ('emailid', 'password')

class RequestListAdmin(admin.ModelAdmin):
	list_display = ('emailid', 'password')

admin.site.register(WebUsers, WebUsersAdmin)
admin.site.register(RequestList, RequestListAdmin)