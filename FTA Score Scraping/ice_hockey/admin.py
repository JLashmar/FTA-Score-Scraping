from django.contrib import admin
from .models import EliteLeagueSchedule, EliteLeagueTable
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(EliteLeagueSchedule)
class EliteLeagueScheduleAdmin(ImportExportModelAdmin):
    pass


@admin.register(EliteLeagueTable)
class EliteLeagueTableAdmin(ImportExportModelAdmin):
    pass

# might need to do resources too
