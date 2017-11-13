from django.apps import apps
from django.test import TestCase
from .apps import TodoitemConfig


class TodoConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(TodoitemConfig.name, 'todoitem')
        self.assertEqual(apps.get_app_config('todoitem').name, 'todoitem')