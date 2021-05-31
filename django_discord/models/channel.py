from django.db import models
from .guild import Guild


class Channel(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    type = models.IntegerField(
        choices=[
            (0, "Guild Text"),
            (1, "Direct Message"),
            (2, "Guild Voice"),
            (3, "Group Direct Message"),
            (4, "Guild Category"),
            (5, "Guild News"),
            (6, "Guild Store"),
            (10, "Guild News Thread"),
            (11, "Guild Public Thread"),
            (12, "Guild Private Thread"),
            (13, "Guild Stage Voice")
        ],
        default=0
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    position = models.IntegerField(default=0)
    name = models.CharField(max_length=128, null=True, default=None)
    topic = models.CharField(max_length=1024, default="")
    nsfw = models.BooleanField(default=False)
    bitrate = models.IntegerField(null=True, default=None)
    user_limit = models.IntegerField(
        verbose_name="User limit of voice channel",
        default=0
    )
    rate_limit_per_user = models.IntegerField(
        default=0
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
