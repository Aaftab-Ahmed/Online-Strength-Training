# Generated by Django 4.1 on 2022-09-14 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0024_auto_20210323_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='setgroup',
            name='order',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]