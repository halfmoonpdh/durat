# Generated by Django 2.1.7 on 2019-04-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brat', '0013_tagingdata_taging_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagingdata',
            name='taging_Data_modified',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
