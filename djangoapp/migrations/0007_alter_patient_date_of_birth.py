# Generated by Django 4.2.16 on 2024-09-23 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
