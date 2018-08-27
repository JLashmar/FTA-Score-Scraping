from import_export import resources
from .models import PGA_Comps PGA_Event
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


class CompetitionResource(resources.ModelResource):
    class Meta:
        model = PGA_Comp


@admin.register(PGA_Comp)
class MasterCategoryAdmin(ImportExportModelAdmin):
    resource_class = CompetitionResource


class EventResource(resources.ModelResource):
    class Meta:
        model = PGA_event


@admin.register(PGA_event)
class EventCategoryAdmin(ImportExportModelAdmin):
    resource_class = EventResource
