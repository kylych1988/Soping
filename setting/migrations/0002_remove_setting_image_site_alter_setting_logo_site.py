# Generated by Django 4.1.3 on 2022-11-22 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='image_site',
        ),
        migrations.AlterField(
            model_name='setting',
            name='logo_site',
            field=models.ImageField(upload_to='logo/'),
        ),
    ]
