# Generated by Django 2.1.13 on 2022-05-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0062_auto_20220510_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='termshistory',
            name='status_version_id',
        ),
        migrations.AddField(
            model_name='termshistory',
            name='status',
            field=models.BooleanField(db_column='Status', default=False),
        ),
    ]