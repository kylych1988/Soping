# Generated by Django 4.1.3 on 2022-11-27 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0018_phone_alter_closis_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='emil_site',
        ),
    ]