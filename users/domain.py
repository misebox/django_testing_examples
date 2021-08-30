import datetime
from typing import List

from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.http.response import HttpResponseForbidden

from djantic import ModelSchema


class UserSchema(ModelSchema):

    class Config:
        model = User
        include = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'last_login',
            'date_joined',
        ]
        class Config:
            json_encoders = {
                datetime.datetime: lambda v: v.isoformat(),
                datetime.date: lambda v: v.isoformat(),
            }


class UserRepository:

    @classmethod
    def find_user_by_name(cls, username: str) -> UserSchema:
        user = User.objects.get(username=username)
        if not user.is_active:
            raise HttpResponseForbidden('User is inactive')
        user_dto = UserSchema(**model_to_dict(user))
        return user_dto

