from django.db import models


class Contact(models.Model):
    name = models.CharField("Ім'я", max_length=100)
    email = models.EmailField("E-mail")

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
