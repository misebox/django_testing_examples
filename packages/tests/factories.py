import datetime

import factory

from packages import models


class ProgrammingLanguageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProgrammingLanguage
    id = factory.Sequence(lambda n: n)
    name = factory.Faker('word')


class PackageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Package
    ref_name = factory.Faker('word')
    name = factory.Faker('word')
    repo_url = factory.Faker('url')
    since_date = datetime.date.today() - datetime.timedelta(days=400)
    pub_date = datetime.datetime.now(datetime.timezone.utc)
    lang = factory.SubFactory(ProgrammingLanguageFactory)


class PackageComboFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.PackageCombo
    name = factory.Faker('word')
    description = factory.Faker('paragraph')

    @factory.post_generation
    def package_set(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for package in extracted:
                self.package_set.add(package)
