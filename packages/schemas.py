from djantic import ModelSchema
from pydantic import BaseModel
from typing import List
from typing import Optional

from packages.models import Package
from packages.models import PackageCombo
from packages.models import ProgrammingLanguage


class ProgrammingLanguageSchema(ModelSchema):
    class Config:
        model = ProgrammingLanguage
        include = ['name']


class PackageSchema(ModelSchema):
    lang: Optional[ProgrammingLanguageSchema]

    class Config:
        model = Package
        include = [
            'name',
            'ref_name',
            'description',
            'repo_url',
            'since_date',
            'pub_date',
            'lang',
        ]

class PackageComboSchema(ModelSchema):
    packages: List[PackageSchema] = []

    class Config:
        model = PackageCombo
        include = [
            'name',
            'description',
            'packages',
        ]


class ComboPageOut(BaseModel):
    packages: List[PackageSchema]
    combos: List[PackageComboSchema]
    langs: List[ProgrammingLanguageSchema]
