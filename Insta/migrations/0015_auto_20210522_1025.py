# Generated by Django 3.2.3 on 2021-05-22 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0014_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='comments',
            field=models.CharField(max_length=2200, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
