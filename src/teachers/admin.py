from django.contrib import admin
from .models import Subjects, Teachers
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class SubjectsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'subject_name',
    )
    list_display_links = ('id', 'subject_name')

admin.site.register(Subjects, SubjectsAdmin)





class TeachersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'room_number',
    )
    list_display_links = ('id', 'first_name','last_name',)
    list_filter = ('first_name','last_name',)

admin.site.register(Teachers, TeachersAdmin)

