# Generated by Django 3.2.3 on 2021-05-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0024_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.ManyToManyField(related_name='posts', to='Insta.Profile'),
        ),
    ]
