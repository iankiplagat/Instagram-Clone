# Generated by Django 3.2.3 on 2021-05-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0030_alter_image_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.ManyToManyField(default=0, null=True, related_name='posts', to='Insta.Profile'),
        ),
    ]
