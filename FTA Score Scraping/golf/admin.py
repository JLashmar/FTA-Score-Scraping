from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import PGA_Comp, PGA_Event
# Register your models here.


@admin.register(PGA_Comp)
class PGACompAdmin(ImportExportModelAdmin):
    pass


@admin.register(PGA_Event)
class PGAEventAdmin(ImportExportModelAdmin):
    pass
