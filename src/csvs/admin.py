from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from teachers.models import Teachers

# Register your models here.
from .models import Csvs

admin.site.register(Csvs)


