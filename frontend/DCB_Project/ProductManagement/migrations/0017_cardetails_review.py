# Generated by Django 4.1.3 on 2024-10-15 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductManagement', '0016_alter_warranty_warranty_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardetails',
            name='review',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approve', 'Approve'), ('Rejected', 'Rejected'), ('Processing', 'Processing')], default='processing', max_length=80),
        ),
    ]
