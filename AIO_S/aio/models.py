from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    Name = models.CharField(max_length=100)
    Phone = PhoneNumberField(region='UZ')


class OfferWork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offer_wrk_user')
    score = models.PositiveSmallIntegerField()
    text = models.CharField(max_length=300)



