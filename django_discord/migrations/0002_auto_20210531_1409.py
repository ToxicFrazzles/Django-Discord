# Generated by Django 3.2.3 on 2021-05-31 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_discord', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='afk_channel',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='django_discord.channel'),
        ),
        migrations.AlterField(
            model_name='guild',
            name='public_updates_channel_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='django_discord.channel'),
        ),
        migrations.AlterField(
            model_name='guild',
            name='rules_channel',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='django_discord.channel'),
        ),
        migrations.AlterField(
            model_name='guild',
            name='system_channel',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='django_discord.channel'),
        ),
        migrations.AlterField(
            model_name='guild',
            name='widget_channel',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='django_discord.channel'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]
