from django.db import models

# Create your models here.
class home(models.Model):
    message = models.CharField(max_length=80)
    def _unicode_(self):
        return self.message
