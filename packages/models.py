from django.db import models


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=30)


class Package(models.Model):
    name = models.CharField(max_length=50)
    ref_name = models.CharField(max_length=50)
    description = models.TextField()
    repo_url = models.URLField(max_length=300)
    since_date = models.DateField()
    pub_date = models.DateTimeField('date published')
    lang = models.ForeignKey(
        'ProgrammingLanguage',
        related_name='package_set',
        on_delete=models.PROTECT
    )


class PackageCombo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    package_set = models.ManyToManyField(
        'package',
        through='PackageComposition',
        through_fields=('package_combo', 'package'),
        related_name='package_combo_set'
    )


class PackageComposition(models.Model):
    description = models.TextField(null=True, blank=True)
    package = models.ForeignKey('Package', on_delete=models.PROTECT)
    package_combo = models.ForeignKey(PackageCombo, on_delete=models.CASCADE)
