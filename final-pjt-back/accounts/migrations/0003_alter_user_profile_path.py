# Generated by Django 3.2.13 on 2022-11-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_profile_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_path',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]