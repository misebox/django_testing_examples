from packages.schemas import ComboPageOut
from packages.repositories import PackageRepository
from packages.repositories import PackageComboRepository


class PackageUsecase:

    @classmethod
    def get_combo_page_context(cls) -> ComboPageOut:
        combos = PackageComboRepository.find_all_package_combos()
        out = ComboPageOut(combos=combos)
        return out
