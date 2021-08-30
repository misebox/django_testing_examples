from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict

from .domain import UserRepository
from .usecases import ShowProfileIn
from .usecases import UserUsecase


@login_required
def profile(request: HttpRequest):
    params = ShowProfileIn(username=request.user.username)
    context = UserUsecase.show_profile(params)
    print(context)
    return render(request, 'users/profile.html', context.dict())
