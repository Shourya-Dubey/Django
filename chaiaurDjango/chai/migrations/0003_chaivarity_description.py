# Generated by Django 5.1.6 on 2025-03-02 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0002_rename_date_addes_chaivarity_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivarity',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
