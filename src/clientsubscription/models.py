from django.db import models
from lib.models import BaseModel
from datetime import date
# Create your models here.


class Client(BaseModel):

    _TYPES = (
        ('monthly','Monthly'),
        ('quarterly','Quarterly'),
        ('yearly','Yearly'),
        ('lifetime','Lifetime')
    )
    first_name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    last_name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    cell_number = models.IntegerField(null=True, blank=True, unique=True)
    plan = models.CharField(max_length=255, null=True, blank=True, choices=_TYPES)
    start_date = models.DateField(null=True, auto_now=False)
    days = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):

        return self.first_name

    def get_days(self):
        if self.plan in ["monthly", "quarterly", "yearly"] and self.start_date:

            delta = date.today() - self.start_date
            return delta.days
        else:
            return "No days"
