from django.db import models


# Create your models here.
class Item(models.Model):
    # form validation max 50 characters, required
    name = models.CharField(max_length=50, null=False, blank=False)
    # form validation, required and default value
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
