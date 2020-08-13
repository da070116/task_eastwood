from django.core.validators import RegexValidator
from django.db import models


class Department(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False, default="")

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, default="")
    patronymic = models.CharField(max_length=50, null=True, blank=True, default="", help_text="Leave blank if none")
    surname = models.CharField(max_length=50, null=False, blank=False, default="")
    birth_date = models.DateField(blank=False, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        validators=[RegexValidator(regex=r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')],
        help_text="Cell phone number is recommended"
    )
    started_work = models.DateField(blank=False, null=True)
    ended_work = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=100, null=False, blank=False, default="")
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, default="")

    def __str__(self):
        if self.patronymic:
            return f"{self.name} {self.patronymic} {self.surname}"
        else:
            return f"{self.name} {self.surname}"
