# Generated by Django 4.1.3 on 2022-11-24 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0004_remove_latest_text_latest_price_alter_latest_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='latest',
            name='image1',
            field=models.ImageField(default=1, upload_to='image_latest/'),
            preserve_default=False,
        ),
    ]
