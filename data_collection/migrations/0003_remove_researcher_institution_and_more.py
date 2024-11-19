# Generated by Django 5.1.2 on 2024-10-24 11:36

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_collection', '0002_researcher_researchproject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researcher',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='researcher',
            name='specialization',
        ),
        migrations.RemoveField(
            model_name='researchproject',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='researchproject',
            name='start_date',
        ),
        migrations.AddField(
            model_name='researcher',
            name='department',
            field=models.CharField(default='General', max_length=255),
        ),
        migrations.AddField(
            model_name='researcher',
            name='phone',
            field=models.CharField(default='0000000000', max_length=15),
        ),
        migrations.AddField(
            model_name='researchproject',
            name='date_started',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='researchproject',
            name='researcher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data_collection.researcher'),
        ),
        migrations.AddField(
            model_name='researchproject',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='researchproject',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='DataCollection',
        ),
    ]
