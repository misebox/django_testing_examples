from django.test import TestCase

from packages.schemas import ComboPageOut
from packages.tests.factories import PackageFactory
from packages.tests.factories import PackageComboFactory
from packages.usecases import PackageUsecase


class PackagesUsecaseTest(TestCase):
    def setUp(self):
        pass

    def test_combo_page_context(self):
        context = PackageUsecase.get_combo_page_context()
        self.assertIsInstance(context, ComboPageOut)
        self.assertEqual(len(context.combos), 0)

    def test_combo_page_context_returns_2_package_combos(self):
        # Create test data with factoryboy (See factories.py)
        p1 = PackageFactory.create()
        p2 = PackageFactory.create()
        p3 = PackageFactory.create()
        PackageComboFactory.create(package_set=(p1, p2))
        PackageComboFactory.create(package_set=(p1, p2, p3))

        context = PackageUsecase.get_combo_page_context()
        self.assertIsInstance(context, ComboPageOut)
