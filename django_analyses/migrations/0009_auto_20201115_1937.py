# Generated by Django 3.1.3 on 2020-11-15 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_analyses', '0008_auto_20201018_1638'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inputspecification',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='outputspecification',
            options={'get_latest_by': 'modified'},
        ),
    ]
