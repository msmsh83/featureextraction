# Generated by Django 2.2 on 2019-05-13 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polygons', '0010_auto_20190510_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='formattedAddress',
            field=models.CharField(blank=True, max_length=256, null=True, unique=True),
        ),
    ]
