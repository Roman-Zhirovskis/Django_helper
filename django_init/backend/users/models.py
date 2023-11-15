from datetime import date
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager, Permission, Group
from django.contrib.auth.hashers import make_password

from base.models import BaseAbstractUser


class CustomerManager(UserManager):
    def _create_customer_user(self, username, email, phone, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        username = CustomerUser.normalize_username(username)
        user = CustomerUser(username=username, email=email, phone=phone, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, phone=None, password=None, **extra_fields):
        return self._create_customer_user(username, email, phone, password, **extra_fields)


class CustomerUser(BaseAbstractUser):
    birthday = models.DateField(_("customer birthday"))
    is_active = models.BooleanField(default=False)
    # country = models.ForeignKey(
    #     Country,
    #     verbose_name="Страна",
    #     on_delete=models.SET_NULL,
    #     null=True,
    # )
    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="customer_user_set",
        related_query_name="customer_user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Permissions for the user"),
        related_name="customer_user_set",
    )
    objects = CustomerManager()

    @property
    def age(self) -> int:
        today: date = date.today()
        age: int = today.year - self.birthday.year

        if today.month < self.birthday.month or (
            today.month == self.birthday.month and today.day < self.birthday.day
        ):
            age -= 1

        return age

    class Meta:
        db_table = "customer"
