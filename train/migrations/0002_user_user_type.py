# Generated by Django 4.1 on 2021-03-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('CL', 'client'), ('TR', 'trainer'), ('AD', 'admin')], default='client', max_length=2, null=True),
        ),
    ]
