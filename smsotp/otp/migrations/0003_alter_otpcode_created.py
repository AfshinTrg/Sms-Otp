# Generated by Django 4.1.1 on 2022-09-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0002_alter_otpcode_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpcode',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]