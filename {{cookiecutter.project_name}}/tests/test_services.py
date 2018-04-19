# -*- coding: utf-8 -*-

from {{cookiecutter.app_name}}.services import UserService


class TestUserServices:
    """ test services """

    def test_auth_and_success(self, user):
        auth_user = UserService.auth(user.username, "myprecious")
        assert auth_user
        assert auth_user.username == user.username

    def test_auth_and_fail(self, user):
        auth_user = UserService.auth(user.username, "myprecious1")
        assert not auth_user

    def test_create_and_success(self, user):
        create_user = UserService.create("for", "for!@", "for@mail.com")
        assert create_user
        assert create_user.username == "for"
