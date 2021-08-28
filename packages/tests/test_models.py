
from django.test.testcases import TestCase

from packages.tests.factories import PackageFactory
from packages.tests.factories import PackageComboFactory
from packages.tests.factories import ProgrammingLanguageFactory


class ProgrammingLanguageTest(TestCase):

    def test___str__(self):
        lang = ProgrammingLanguageFactory(id=10, name='Python')
        self.assertEqual(str(lang), '10:Python')


class PackageTest(TestCase):

    def test___str__(self):
        package = PackageFactory(id=20, name='package-name')
        self.assertEqual(str(package), '20:package-name')


class PackageComboTest(TestCase):

    def test___str__(self):
        combo = PackageComboFactory(id=30, name='combo-name')
        self.assertEqual(str(combo), '30:combo-name')
