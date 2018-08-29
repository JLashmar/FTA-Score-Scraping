from import_export import resources
from .models import RFU_Fixtures, RFU_Table
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


class CompetitionResource(resources.ModelResource):
    class Meta:
        model = RFU_Fixtures


@admin.register(PGA_Comp)
class MasterCategoryAdmin(ImportExportModelAdmin):
    resource_class = CompetitionResource


class TableResource(resources.ModelResource):
    class Meta:
        model = RFU_Table


@admin.register(PGA_event)
class EventCategoryAdmin(ImportExportModelAdmin):
    resource_class = TableResource
