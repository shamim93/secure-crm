import bcrypt
from django.conf import settings
from django.contrib.auth.hashers import BasePasswordHasher
from django.utils.translation import gettext_noop as _


class BcryptPepperHasher(BasePasswordHasher):
    algorithm = "bcrypt_pepper"

    def salt(self):
        return bcrypt.gensalt().decode()

    def encode(self, password, salt=None):
        peppered = (password + settings.PASSWORD_PEPPER).encode()
        hashed = bcrypt.hashpw(peppered, bcrypt.gensalt())
        return f"{self.algorithm}${hashed.decode()}"

    def verify(self, password, encoded):
        try:
            algorithm, hashed = encoded.split('$', 1)
        except ValueError:
            return False
        peppered = (password + settings.PASSWORD_PEPPER).encode()
        return bcrypt.checkpw(peppered, hashed.encode())

    def safe_summary(self, encoded):
        try:
            algorithm, hashed = encoded.split('$', 1)
        except ValueError:
            return {
                _('algorithm'): self.algorithm,
                _('hash'): 'invalid'
            }
        return {
            _('algorithm'): algorithm,
            _('hash'): hashed[:6] + "..."
        }

    def must_update(self, encoded):
        return False
