from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Competition, Result
# Register your models here.

admin.site.register(Result)


@admin.register(Competition)
class CompetitionAdmin(ImportExportModelAdmin):
    pass
