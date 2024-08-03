# Generated by Django 5.0.4 on 2024-06-30 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_studentmodel_got_recommended_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='got_recommended_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advertisement', to='api.advertisementmodel'),
        ),
        migrations.AlterField(
            model_name='studentpaymentmodel',
            name='paid_payment',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=16),
        ),
    ]
