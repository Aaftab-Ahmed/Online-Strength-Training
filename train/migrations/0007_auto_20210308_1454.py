# Generated by Django 4.1 on 2022-09-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0006_auto_20210308_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setgroup',
            name='note',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
