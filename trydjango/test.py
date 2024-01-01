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

# idk if this is ok
policy = PasswordPolicy.from_names(
            length=32,  # at least 32 characters long
            uppercase=1,  # at least 1 uppercase letter
            numbers=1,  # at least 1 digit
            special=1,  # at least 1 special character
        )

        # Check if the secret key meets the password policy
        errors = [error for error in policy.test(SECRET_KEY)]
        self.assertEqual(len(errors), 0, f"Secret key is weak. Errors: {errors}")
