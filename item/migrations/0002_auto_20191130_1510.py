# Generated by Django 2.1.5 on 2019-11-30 12:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_id',
            new_name='item_idd',
        ),
        migrations.AlterField(
            model_name='promocode',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 30, 12, 10, 5, 972231, tzinfo=utc), verbose_name='Срок действия безлимитного кода'),
        ),
    ]
