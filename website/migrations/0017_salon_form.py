# Generated by Django 2.0.2 on 2018-05-20 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_headline'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='need_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='salon',
            name='need_phone_number',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='salonregistration',
            name='contestant_name',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salonregistration',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='salonregistration',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
