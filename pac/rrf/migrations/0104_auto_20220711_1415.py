# Generated by Django 2.1.13 on 2022-07-11 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0103_auto_20220711_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_type',
            field=models.TextField(db_column='ReviewType', default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='reviewhistory',
            name='review_type',
            field=models.TextField(db_column='ReviewType', default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='sales_incentive_id',
            field=models.ForeignKey(db_column='SalesIncentiveID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.SalesIncentive'),
        ),
        migrations.AlterField(
            model_name='reviewhistory',
            name='sales_incentive_version_id',
            field=models.ForeignKey(db_column='SalesIncentiveVersionID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.SalesIncentiveHistory'),
        ),
    ]