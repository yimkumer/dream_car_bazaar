# Generated by Django 4.1.3 on 2024-10-22 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductManagement', '0020_lead_user_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='explored_pages',
            new_name='visit_count',
        ),
    ]
