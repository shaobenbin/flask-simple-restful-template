# -*- coding: utf-8 -*-
"""Functional tests using WebTest.

See: http://webtest.readthedocs.org/
"""

import json


class TestLoggingIn:

    """ Login. """
    def test_can_login_and_success(self, user, testapp):
        """ Login successful. """
        resp = testapp.post_json('/api/v1.0/login', dict(username=user.username, password='myprecious'))
        assert resp.status_code == 200
        assert json.loads(resp.text)['state'] == 1

    def test_login_fail_cause_password_error(self, user, testapp):
        """ Login fail cause password error. """
        resp = testapp.post_json('/api/v1.0/login', dict(username=user.username, password='fail'))
        assert resp.status_code == 200
        assert json.loads(resp.text)['state'] == 0

    def test_login_fail_cause_username_error(self, user, testapp):
        """ Login fail cause username error. """
        resp = testapp.post_json('/api/v1.0/login', dict(username="fail", password='myprecious'))
        assert resp.status_code == 200
        assert json.loads(resp.text)['state'] == 0

    def test_logout_and_success(self, user, testapp):
        testapp.post_json('/api/v1.0/login', dict(username=user.username, password='myprecious'))
        resp = testapp.get('/api/v1.0/logout')
        assert resp.status_code == 200
        assert json.loads(resp.text)['state'] == 1

    def test_security_content(self, user, testapp):
        testapp.post_json('/api/v1.0/login', dict(username=user.username, password='myprecious'))
        resp = testapp.get('/api/v1.0/security/test')
        assert resp.status_code == 200
        assert 'security content' in resp.text


class TestRegistering:
    """Register a user."""
    def test_register_and_success(self, user, testapp):
        resp = testapp.post_json('/api/v1.0/register', dict(username="foobar", password='secret', email='foo@bar.com'))
        assert resp.status_code == 200
        assert json.loads(resp.text)['state'] == 1


class TestHome:
    """ Just test home page """
    def test_home(self, testapp):
        resp = testapp.get("/")
        assert resp.status_code == 200
        assert 'HelloWorld' == resp.text
