from django.contrib import admin
from accounts.models import students_data
from import_export.admin import ImportExportModelAdmin
from import_export import resources


# Register your models here.
class StudentResource(resources.ModelResource):

    class Meta:
        model = students_data
        import_id_fields = ('roll_no',)


class StudentsDataAdmin(ImportExportModelAdmin,students_data):
    list_filter = ('roll_no', 'team_no', 'score',)
    list_display = ('name', 'roll_no', 'score', 'team_no',)


# admin.site.register(students_data)
admin.site.register(students_data, StudentsDataAdmin)
