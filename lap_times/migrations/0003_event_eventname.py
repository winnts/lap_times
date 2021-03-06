# Generated by Django 3.1.2 on 2020-10-14 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lap_times', '0002_auto_20201014_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_time', models.DurationField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lap_times.car')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lap_times.driver')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lap_times.eventname')),
            ],
        ),
    ]
