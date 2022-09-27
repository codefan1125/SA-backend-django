# Generated by Django 2.1.13 on 2022-09-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pac', '0033_auto_20220907_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_new',
            field=models.BooleanField(db_column='IsNew', default=True),
        ),
        migrations.AddField(
            model_name='notificationhistory',
            name='is_new',
            field=models.BooleanField(db_column='IsNew', default=False),
            preserve_default=False,
        ),
    ]