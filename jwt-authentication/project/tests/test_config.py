# project/server/tests/test_config.py

import unittest

from flask import current_app
from flask_testing import TestCase

from project.server import app

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is '\xd15\xfe%\x98\xd9\x13\xbaC|\xe6\xe0\x18\x82\x11\xce\x84\xe4R\xf56a\xb5o')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://hello_flask:hello_flask@db:5432/hello_flask_prod'
    )

class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] is '\xd15\xfe%\x98\xd9\x13\xbaC|\xe6\xe0\x18\x82\x11\xce\x84\xe4R\xf56a\xb5o')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://hello_flask:hello_flask@db:5432/hello_flask_prod'
        )

class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()