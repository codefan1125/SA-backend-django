# Generated by Django 2.1.13 on 2022-06-17 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0083_auto_20220617_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_owner',
            field=models.ForeignKey(blank=True, db_column='RequestOwner', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='request',
            name='submitted_by',
            field=models.ForeignKey(blank=True, db_column='SubmittedBy', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]