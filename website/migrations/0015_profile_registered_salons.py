# Generated by Django 2.0.2 on 2018-05-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_home_tab'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='registered_salons',
            field=models.ManyToManyField(blank=True, related_name='attendees', to='website.Salon'),
        ),
    ]
