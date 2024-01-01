import os
from django.conf import Settings
from django.contrib.auth.password_validation import validate_password#django validation method
from django.test import TestCase

class ConfigTest(TestCase):
    def test_secret_key_strength(self):
        SECRET_KEY = os.environ.get( 'DJANGO_SECRET_KEY')  
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'secret key is not strong{e.messages}'
            self.fail(msg)

