from django.test import TestCase

from packages.schemas import PackageComboSchema
from packages.repositories import PackageComboRepository
from packages.repositories import PackageRepository
from packages.tests.factories import PackageFactory
from packages.tests.factories import PackageComboFactory


class PackageComboRepositoryTest(TestCase):

    def test_find_all_packages(self):
        # empty
        packages = PackageRepository.find_all_packages()
        self.assertEqual(len(packages), 0)

        # 1 package
        p1 = PackageFactory.create()
        packages = PackageRepository.find_all_packages()
        self.assertEqual(len(packages), 1)
        self.assertEqual(packages[0].name, p1.name)
        self.assertEqual(packages[0].description, p1.description)

        # 3 packages
        p2 = PackageFactory.create()
        p3 = PackageFactory.create()
        packages = PackageRepository.find_all_packages()
        self.assertEqual(len(packages), 3)

    def test_find_all_package_combos(self):
        # Create test data with factoryboy (See factories.py)
        p1 = PackageFactory.create()
        p2 = PackageFactory.create()
        p3 = PackageFactory.create()
        PackageComboFactory.create(name='combo1', package_set=(p1, p2))
        combos = PackageComboRepository.find_all_package_combos()
        self.assertEqual(len(combos), 1)
        self.assertEqual(combos[0].name, 'combo1')
        self.assertIsInstance(combos[0], PackageComboSchema)

        # one more PackageCombo
        PackageComboFactory.create(package_set=(p1, p2, p3))
        combos = PackageComboRepository.find_all_package_combos()
        self.assertEqual(len(combos), 2)
