from django.db import models


class Veri(models.Model):
    kilo = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    boy = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    class Meta:
        get_latest_by = 'id'
