from django.test import TestCase

from packages.schemas import PackageComboSchema
from packages.repositories import PackageRepository
from packages.repositories import PackageComboRepository
from packages.tests.factories import PackageFactory
from packages.tests.factories import PackageComboFactory


class PackageComboRepositoryTest(TestCase):

    def test_find_all_package_combos(self):
        # Create test data with factoryboy (See factories.py)
        p1 = PackageFactory.create()
        p2 = PackageFactory.create()
        p3 = PackageFactory.create()
        PackageComboFactory.create(package_set=(p1, p2))
        PackageComboFactory.create(package_set=(p1, p2, p3))
        combos = PackageComboRepository.find_all_package_combos()
        self.assertEqual(len(combos), 2)
        self.assertIsInstance(combos[0], PackageComboSchema)
