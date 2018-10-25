from django.db import models
from django.contrib.auth import models as auth_models


class Contact(models.Model):
    name = models.CharField("Ім'я", max_length=100)
    email = models.EmailField("E-mail")
    user = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакти'

    def __str__(self):
        return self.name


class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    number = models.IntegerField()

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номери'
