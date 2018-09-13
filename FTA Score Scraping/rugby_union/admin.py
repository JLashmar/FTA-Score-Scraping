from django.contrib import admin
from .models import RFU_Fixtures, RFU_Table, Premier15Fixtures, Premier15Results, Premier15Table
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(RFU_Fixtures)
class PGACompAdmin(ImportExportModelAdmin):
    pass


@admin.register(RFU_Table)
class PGAEventAdmin(ImportExportModelAdmin):
    pass


@admin.register(Premier15Fixtures)
class Premier15FixtureAdmin(ImportExportModelAdmin):
    pass


@admin.register(Premier15Results)
class Premier15ResultsAdmin(ImportExportModelAdmin):
    pass


@admin.register(Premier15Table)
class Premier15TableAdmin(ImportExportModelAdmin):
    pass
