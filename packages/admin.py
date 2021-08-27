from django.contrib import admin

from . import models


class ProgrammingLanguageAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


class PackageCompositionInline(admin.TabularInline):
    model = models.PackageComposition


class PackageAdmin(admin.ModelAdmin):
    fields = ('name', 'ref_name', 'description', 'repo_url', 'since_date', 'pub_date', 'lang')
    list_display = ('name', 'ref_name', 'repo_url', 'since_date', 'pub_date', 'lang')


class PackageComboAdmin(admin.ModelAdmin):
    inlines = [
        PackageCompositionInline
    ]
    def package_count(self, obj):
        return obj.package_set.count()
    fields = ('name', 'description',)
    list_display = ('name', 'package_count', 'description')


admin.site.register(models.ProgrammingLanguage, ProgrammingLanguageAdmin)
admin.site.register(models.Package, PackageAdmin)
admin.site.register(models.PackageCombo, PackageComboAdmin)
admin.site.register(models.PackageComposition)
