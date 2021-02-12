# Generated by Django 3.0.8 on 2020-10-09 05:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_results', '0007_remove_taskresult_hidden'),
        ('django_analyses', '0006_auto_20200929_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysisversion',
            name='max_parallel',
            field=models.PositiveIntegerField(default=4),
        ),
        migrations.AddField(
            model_name='run',
            name='task_result',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_celery_results.TaskResult'),
        ),
    ]
