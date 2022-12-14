# Generated by Django 4.1.3 on 2022-11-22 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_site', models.CharField(max_length=200)),
                ('description_site', models.CharField(max_length=150)),
                ('logo_site', models.ImageField(upload_to='logo')),
                ('image_site', models.ImageField(upload_to='image')),
                ('phone_site', models.CharField(max_length=200)),
                ('emil_site', models.EmailField(max_length=254)),
                ('instagram_site', models.URLField()),
            ],
        ),
    ]
