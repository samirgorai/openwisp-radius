# Generated by Django 3.1.8 on 2021-11-19 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_radius', '0024_sms_verification'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationradiussettings',
            name='login_url',
            field=models.URLField(
                verbose_name='Login URL',
                blank=True,
                help_text='Enter the URL where users can log in to the wifi service',
                null=True,
            ),
        ),
        migrations.AddField(
            model_name='organizationradiussettings',
            name='status_url',
            field=models.URLField(
                blank=True,
                help_text='Enter the URL where users can log out from the wifi service',
                null=True,
                verbose_name='Status URL',
            ),
        ),
    ]
