from django.contrib import admin
from .models import RFU_Fixtures, RFU_Table
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(RFU_Fixtures)
class PGACompAdmin(ImportExportModelAdmin):
    pass


@admin.register(RFU_Table)
class PGAEventAdmin(ImportExportModelAdmin):
    pass
