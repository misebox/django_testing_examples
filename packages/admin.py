from django.contrib import admin

from . import models

admin.site.register(models.ProgrammingLanguage)
admin.site.register(models.Package)
admin.site.register(models.PackageCombo)
admin.site.register(models.PackageComposition)
