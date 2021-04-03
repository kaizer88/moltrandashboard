# from django.db import models
# from lib.models import BaseModel
#
# from propertyrentals.models import Province
#
# # Create your models here.
#
# class Metro(models.Model):
#     name = models.CharField(max_length=255, unique=True, null=False, blank=False)
#     code = models.CharField(max_length=5, unique=True, null=False, blank=False)
#     province = models.ForeignKey('propertyrentals.Province', on_delete=models.CASCADE, null=False, blank=False)
#
#     def __str__(self):
#         return self.name
#
# class District(models.Model):
#     name = models.CharField(max_length=255, unique=True, null=False, blank=False)
#     code = models.CharField(max_length=5, unique=True, null=False, blank=False)
#     metro = models.ForeignKey('Metro', on_delete=models.CASCADE, null=False, blank=False)
#
#     def __str__(self):
#         return self.name
#
# class Local(models.Model):
#     name = models.CharField(max_length=255, unique=True, null=False, blank=False)
#     code = models.CharField(max_length=5, unique=True, null=False, blank=False)
#     district = models.ForeignKey('District', on_delete=models.CASCADE, null=False, blank=False)
#
#     def __str__(self):
#         return self.name
#
# class Ward(models.Model):
#     name = models.CharField(max_length=255, unique=True, null=False, blank=False)
#     code = models.CharField(max_length=5, unique=True, null=False, blank=False)
#     local = models.ForeignKey('Local', on_delete=models.CASCADE, null=False, blank=False)
#
#     def __str__(self):
#         return self.name