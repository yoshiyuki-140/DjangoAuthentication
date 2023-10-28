# this is user model sample code
# this code will be not used

from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _


class AbstractBaseUser(models.Model):
    password = models.CharField(_('username'), max_length=128)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)
    is_active = True
    REQUIRED_FIEDS = []

    class Meta:
        abstract = True


class AbstractUser(AbstractBaseUser, PermissionMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'), max_length=150, unique=True, validators=[username_validator])
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FILEDS = ['email']

    class Meta:
        abstract = True


class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
