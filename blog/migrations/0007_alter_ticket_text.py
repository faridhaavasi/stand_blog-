# Generated by Django 4.1.2 on 2022-12-15 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_ticket_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
