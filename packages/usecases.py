from packages.schemas import ComboPageOut
from packages.repositories import PackageRepository
from packages.repositories import PackageComboRepository


def combo_page_context() -> ComboPageOut:
    packages = PackageRepository.find_all_packages()
    combos = PackageComboRepository.find_all_package_combos()
    out = ComboPageOut(packages=packages, combos=combos, langs=[])
    return out
