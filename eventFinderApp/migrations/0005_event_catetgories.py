# Generated by Django 2.2 on 2019-09-14 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0004_event_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='catetgories',
            field=models.ManyToManyField(to='eventFinderApp.Category'),
        ),
    ]
