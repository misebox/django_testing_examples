from typing import List

from django.db.models import Prefetch
from django.db.models import Count
from django.forms.models import model_to_dict

from packages.schemas import PackageSchema
from packages.schemas import PackageComboSchema
from packages.schemas import ProgrammingLanguageSchema
from packages import models


class PackageRepository:

    @classmethod
    def find_all_packages(cls) -> List[PackageSchema]:
        packages = models.Package.objects\
            .select_related('lang')\
            .annotate(package_combo_set_count=Count('package_combo_set'))\
            .all()
        return [PackageSchema.from_django(p) for p in packages]


class PackageComboRepository:

    @classmethod
    def find_all_package_combos(cls) -> List[PackageComboSchema]:
        # Use prefetch to avoid N+1 problem
        package_queryset = (models.Package.objects
                            .select_related('lang')
                            .order_by('package_combo_set', 'lang__name', 'name')
                            )
        pre_packages = Prefetch('package_set',
                                queryset=package_queryset,
                                to_attr='packages')
        combos_queryset = models.PackageCombo.objects\
            .prefetch_related(pre_packages)\
            .all()
        combos = []
        for combo_obj in combos_queryset:
            packages = []
            for package_obj in combo_obj.packages:
                package = PackageSchema.from_django(package_obj)
                # Use select_related attribute
                package.lang = ProgrammingLanguageSchema.from_django(
                    package_obj.lang)
                packages.append(package)
            combo = PackageComboSchema.from_django(combo_obj)
            # Use prefetched attribute `packages`
            combo.packages = packages
            combos.append(combo)

        return combos
