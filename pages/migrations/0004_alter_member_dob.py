# Generated by Django 4.2.20 on 2025-03-26 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_member_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='dob',
            field=models.CharField(max_length=10),
        ),
    ]
