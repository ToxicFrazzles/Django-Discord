import django
from django.db import models


class User(models.Model):
    id = models.PositiveBigIntegerField(
        verbose_name="Discord User ID",
        primary_key=True
    )
    # A discord user has to have a username, discriminator etc. but that
    # information might not have been collected at the time of adding the user
    # ID into the database. So we allow them to be null and default to null
    username = models.CharField(
        max_length=32,
        null=True,
        default=None
    )
    discriminator = models.CharField(
        max_length=4,
        null=True,
        default=None
    )
    avatar = models.CharField(
        max_length=64,
        null=True,
        default=None,
        blank=True
    )
    bot = models.BooleanField(
        verbose_name="Is the user a bot?", name="Bot?",
        default=False
    )
    system = models.BooleanField(
        verbose_name="Is the user a system user?", name="System User?",
        default=False
    )
    mfa_enabled = models.BooleanField(
        name="MFA Enabled?",
        default=False
    )
    locale = models.CharField(
        max_length=64,
        default="",
        blank=True
    )
    verified = models.BooleanField(
        verbose_name="Email on the account verified?",
        name="Verified?",
        default=False
    )
    email = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        default=None
    )
    flags = models.IntegerField(
        default=0
    )
    premium_type = models.IntegerField(
        default=0
    )
    public_flags = models.IntegerField(
        default=0
    )
