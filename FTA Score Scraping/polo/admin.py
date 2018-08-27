from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Competition, Result, MyComp
# Register your models here.


@admin.register(MyComp)
class MyCompetitionAdmin(ImportExportModelAdmin):
    pass


@admin.register(Competition)
class CompetitionAdmin(ImportExportModelAdmin):
    pass


@admin.register(Result)
class MyCompetitionAdmin(ImportExportModelAdmin):
    pass
