# Generated by Django 5.0.4 on 2024-05-01 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0004_startap_deposit_amount_startap_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startap',
            name='deposit_amount',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0, verbose_name='Сумма вклада'),
        ),
    ]