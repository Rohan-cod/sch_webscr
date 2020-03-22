from django.contrib import admin

# Register your models here.

from .models import Job_posting

class Job_postingAdmin(admin.ModelAdmin):
    class Meta:
	    model = Job_posting

admin.site.register(Job_posting,Job_postingAdmin)