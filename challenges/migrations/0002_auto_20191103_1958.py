# Generated by Django 2.2.6 on 2019-11-03 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation_to_challenge',
            name='invitees',
            field=models.ManyToManyField(help_text='invite as many people to the challenge!', related_name='Invitation', through='challenges.Invitation_status', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invitation_to_challenge',
            name='invitor_user_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invitation_status',
            name='invitation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='challenges.Invitation_to_challenge'),
        ),
        migrations.AddField(
            model_name='invitation_status',
            name='invitee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='challenge',
            name='invitations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='challenges.Invitation_to_challenge'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='challenges', to=settings.AUTH_USER_MODEL),
        ),
    ]
