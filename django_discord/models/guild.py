from django.db import models
from .user import User
from .channel import Channel


class Guild(models.Model):
    id = models.PositiveBigIntegerField(
        verbose_name="Discord Guild ID",
        primary_key=True
    )
    # A discord guild has to have a name etc. but that
    # information might not have been collected at the time of adding the guild
    # ID into the database. So we allow them to be null and default to null
    name = models.CharField(
        max_length=128,
        null=True,
        default=None
    )
    icon = models.CharField(
        max_length=64,
        null=True,
        default=None
    )
    splash = models.CharField(
        max_length=64,
        null=True,
        default=None
    )
    discovery_splash = models.CharField(
        max_length=64,
        null=True,
        default=None
    )

    # This is where the model deviates from the discord spec
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    afk_channel = models.ForeignKey(Channel, on_delete=models.SET_NULL)

    region = models.CharField(
        max_length=16,
        null=True,
        default=None
    )
    afk_timeout = models.IntegerField(
        verbose_name="AFK Timeout in Seconds",
        null=True,
        default=None
    )
    widget_enabled = models.BooleanField(
        verbose_name="Is the Widget Enabled?",
        name="Widget Enabled?",
        default=False
    )
    widget_channel = models.ForeignKey(Channel, on_delete=models.SET_NULL)
    verification_level = models.IntegerField(
        choices=[
            (0, "None"),
            (1, "Low"),
            (2, "Medium"),
            (3, "High"),
            (4, "Very High")
        ],
        default=0
    )
    default_message_notifications = models.IntegerField(
        choices=[
            (0, "All Messages"),
            (1, "Only Mentions")
        ],
        default=0
    )
    explicit_content_filter = models.IntegerField(
        choices=[
            (0, "Disabled"),
            (1, "Members Without Roles"),
            (2, "All Members")
        ],
        default=0
    )
    mfa_level = models.IntegerField(
        choices=[
            (0, "None"),
            (1, "Elevated")
        ],
        default=0
    )
    application = models.PositiveBigIntegerField(null=True, default=None)
    system_channel = models.ForeignKey(
        Channel,
        on_delete=models.SET_NULL,
        null=True
    )
    system_channel_flags = models.IntegerField(default=0)
    rules_channel = models.ForeignKey(
        Channel,
        on_delete=models.SET_NULL
    )
    large = models.BooleanField(name="Large?", default=False)
    vanity_url_code = models.CharField(max_length=64, null=True, default=None)
    description = models.CharField(max_length=512, default="")
    banner = models.CharField(max_length=64, null=True, default=None)
    premium_tier = models.IntegerField(
        choices=[
            (0, "None"),
            (1, "Tier 1"),
            (2, "Tier 2"),
            (3, "Tier 3")
        ],
        default=0
    )
    premium_subscription_count = models.IntegerField(default=0)
    preferred_locale = models.CharField(max_length=16, null=True, default=None)
    public_updates_channel_id = models.ForeignKey(
        Channel,
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    nsfw_level = models.IntegerField(
        choices=[
            (0, "Default"),
            (1, "Explicit"),
            (2, "Safe"),
            (3, "Age Restricted")
        ],
        default=0
    )
