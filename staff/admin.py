from django.contrib import admin
from .models import Staff

class StaffAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Staff._meta.fields]
    search_fields = ['last_name', 'first_name', 'middle_name', ]

    class Meta:
        model = Staff

admin.site.register(Staff, StaffAdmin)
