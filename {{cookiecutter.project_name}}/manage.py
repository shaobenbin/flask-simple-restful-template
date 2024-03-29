# -*- coding: utf-8 -*-
"""Create an application instance."""

import os
from flask.helpers import get_debug_flag
from flask_script import Shell, Server
from flask_script.commands import Clean, ShowUrls
from {{cookiecutter.app_name}}.conf.settings import DevConfig, ProdConfig
from flask_migrate import MigrateCommand
from flask_script import Manager
from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.app import db
from {{cookiecutter.app_name}}.models import User


print(get_debug_flag())
CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)
manager = Manager(app)

HERE = os.path.abspath(os.path.dirname(__file__))
TEST_PATH = os.path.join(HERE, 'tests')


def _make_context():
    """Return context dict for a shell session so you can access
    app, db, and the User model by default.
    """
    return {'app': app, 'db': db, 'User': User}


@app.after_request
def after_request(response):
    # 使用nginx的反向代理来解决是最完美的
    return response


@manager.command
def test():
    """Run the tests."""
    import pytest
    exit_code = pytest.main([TEST_PATH, '--verbose'])
    return exit_code


manager.add_command('server', Server())
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)
manager.add_command("urls", ShowUrls())
manager.add_command("clean", Clean())

if __name__ == "__main__":
    manager.run()
