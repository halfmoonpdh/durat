# Generated by Django 2.1.7 on 2019-05-13 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brat', '0020_auto_20190513_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='latesttagingdata',
            name='latest_taging_title',
            field=models.CharField(default='', max_length=60),
        ),
    ]
