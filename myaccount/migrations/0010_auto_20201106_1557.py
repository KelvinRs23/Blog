# Generated by Django 3.1.2 on 2020-11-06 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0009_image_desk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='desk',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
