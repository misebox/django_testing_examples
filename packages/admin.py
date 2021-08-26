from django.contrib import admin

from . import models


class ProgrammingLanguageAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)

class PackageAdmin(admin.ModelAdmin):
    fields = ('name', 'ref_name', 'description', 'repo_url', 'since_date', 'pub_date', 'lang')
    list_display = ('name', 'ref_name', 'repo_url', 'since_date', 'pub_date', 'lang')

class PackageComboAdmin(admin.ModelAdmin):
    fields = ('name', 'description',)
    filter_horizontal = ['package_set']

admin.site.register(models.ProgrammingLanguage, ProgrammingLanguageAdmin)
admin.site.register(models.Package, PackageAdmin)
admin.site.register(models.PackageCombo, PackageComboAdmin)
admin.site.register(models.PackageComposition)
