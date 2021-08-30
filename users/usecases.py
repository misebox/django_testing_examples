import datetime
from pydantic import BaseModel

from .domain import UserRepository
from .domain import UserSchema


class ShowProfileIn(BaseModel):
    username: str


class ShowProfileOut(BaseModel):
    user: UserSchema


class UserUsecase:

    def show_profile(params: ShowProfileIn) -> ShowProfileOut:
        user_dto = UserRepository.find_user_by_name(params.username)
        out = ShowProfileOut(user=user_dto.dict())
        return out
