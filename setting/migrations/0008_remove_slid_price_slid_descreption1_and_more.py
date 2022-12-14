# Generated by Django 4.1.3 on 2022-11-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0007_remove_slid_descreption1_remove_slid_descreption2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slid',
            name='price',
        ),
        migrations.AddField(
            model_name='slid',
            name='descreption1',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slid',
            name='descreption2',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slid',
            name='image1',
            field=models.ImageField(default=1, upload_to='image/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slid',
            name='image2',
            field=models.ImageField(default=1, upload_to='image/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slid',
            name='name1',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slid',
            name='name2',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
