# Generated by Django 2.1.13 on 2021-02-18 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0027_requesthistory_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestsectionlaneimportqueue',
            name='initial_rec_order',
            field=models.IntegerField(db_column='InitialRecOrder', null=True),
        ),
        migrations.AddField(
            model_name='requestsectionlanepricingpointimportqueue',
            name='initial_rec_order',
            field=models.IntegerField(db_column='InitialRecOrder', null=True),
        ),
    ]