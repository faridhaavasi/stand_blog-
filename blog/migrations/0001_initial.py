# Generated by Django 4.1.2 on 2022-10-30 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('body', models.TextField()),
                ('img', models.ImageField(upload_to='images/blog/post')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('d', 'draft'), ('p', 'publish')], default='d', max_length=1)),
            ],
        ),
    ]