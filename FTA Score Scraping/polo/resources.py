from import_export import resources
from .models import Competition
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


class CompetitionResource(resources.ModelResource):
    class Meta:
        model = Competition


@admin.register(Competition)
class MasterCategoryAdmin(ImportExportModelAdmin):
    resource_class = CompetitionResource
