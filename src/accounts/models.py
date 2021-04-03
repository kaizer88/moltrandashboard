from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, User
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# class MyRole(models.Model):
#
#     name = models.CharField(max_length=20, null=False, blank=False)
#     desc = models.CharField(max_length=20, null=True, blank=True)
#
#     def __str__(self):
#         return self.name

class User(AbstractUser):
  roles = models.ManyToManyField(Role)

class Profile(AbstractUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True,default=None)
    cell_number = models.IntegerField(null=True, blank=True)
    # kin_number = models.IntegerField(null=True, blank=True)
    # kin_first_name = models.CharField(max_length=30, null=True, blank=True)
    # kin_last_name = models.CharField(max_length=30, null=True, blank=True)
    # details = models.CharField(max_length=20, null=True, blank=True)

    # school_place = models.ForeignKey('appadmin.School', on_delete=models.CASCADE, null = True, blank = True)
    # work = models.ProtectedForeignKey('MyRole', null = True, blank = True)

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        full_name = "{} {}".format(self.first_name, self.last_name) \
            if self.first_name and self.last_name else \
            "{}".format(self.first_name) if self.first_name \
                else "{}".format(self.last_name) if self.last_name \
                else None
        return full_name