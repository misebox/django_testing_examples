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
        ProgrammingLanguage,
        related_name='packages',
        on_delete=models.PROTECT
    )
    combo_set = models.ManyToManyField(
        'combo',
        through='composition',
        through_fields=('package', 'combo'),
        related_name='package_set',
    )


class Combo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Composition(models.Model):
    description = models.TextField(null=True, blank=True)
    package = models.ForeignKey(Package, on_delete=models.PROTECT)
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE)
