# Generated by Django 5.1 on 2024-09-02 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egyanportal', '0015_alter_registration_new_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='new_file',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
