from django.contrib import admin
from home.models import Contact
from home.models import Newsletter
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Contact)
@admin.register(Newsletter)
class usremail(ImportExportModelAdmin):
    pass

class contactsemail(ImportExportModelAdmin):
    pass