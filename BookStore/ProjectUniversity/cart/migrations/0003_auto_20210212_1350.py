# Generated by Django 3.1.6 on 2021-02-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20210212_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='refund_granted',
        ),
        migrations.RemoveField(
            model_name='order',
            name='refund_requested',
        ),
        migrations.AlterField(
            model_name='order',
            name='being_delivered',
            field=models.BooleanField(default=False, verbose_name='ارسال'),
        ),
        migrations.AlterField(
            model_name='order',
            name='received',
            field=models.BooleanField(default=False, verbose_name='دریافت'),
        ),
    ]
