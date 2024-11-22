from django.db import models
from django.conf import settings
from cryptography.fernet import Fernet

# Create your models here.

_CYPHER = Fernet(settings.FERNET_KEY)

class API(models.Model):
    name = models.CharField(max_length=100, unique=True)
    key = models.CharField(max_length=100, editable=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.key:
            self.key = _CYPHER.encrypt(self.key.encode()).decode()
        super(API, self).save(*args, **kwargs)

    def get_decrypted_key(self):
        return _CYPHER.decrypt(self.key.encode()).decode()

    def __str__(self):
        return self.name