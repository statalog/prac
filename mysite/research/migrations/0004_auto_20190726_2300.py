# Generated by Django 2.0.13 on 2019-07-27 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0003_auto_20190722_1844'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Research',
            new_name='Study',
        ),
        migrations.AlterModelOptions(
            name='study',
            options={'verbose_name_plural': 'studies'},
        ),
    ]
