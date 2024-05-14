# Generated by Django 5.0.4 on 2024-05-01 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0003_alter_categorystartap_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='startap',
            name='deposit_amount',
            field=models.PositiveSmallIntegerField(blank=True, db_index=True, default=0, verbose_name='Сумма вклада'),
        ),
        migrations.AddField(
            model_name='startap',
            name='location',
            field=models.CharField(blank=True, db_index=True, default='', max_length=50, verbose_name='Местоположение'),
        ),
    ]