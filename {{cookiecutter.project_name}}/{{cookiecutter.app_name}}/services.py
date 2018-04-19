# -*- coding: utf-8 -*-

from {{cookiecutter.app_name}}.models import User


class UserService:

    def __init__(self):
        pass

    @classmethod
    def auth(cls, username, password):
        user = User.query.filter_by(username=username).first()
        if not user:
            return None

        if user.check_password(password):
            return user

        return None

    @classmethod
    def create(cls, username, password, email):
        user = User.create(username=username, password=password, email=email)
        return user
