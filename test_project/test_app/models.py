from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=2555)
