# Generated by Django 4.2.16 on 2024-09-27 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0023_alter_doctor_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateField(auto_now_add=True)),
                ('medication', models.TextField()),
                ('dosage', models.CharField(max_length=100)),
                ('instructions', models.TextField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('appointment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoapp.appointment')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.patient')),
            ],
        ),
    ]
