# Generated by Django 2.2 on 2019-04-09 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polygons', '0005_auto_20190408_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='boundery',
            name='matchingId',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]