# Generated by Django 3.2.3 on 2021-05-20 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0003_alter_image_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='comments',
            field=models.CharField(default='', max_length=2200),
        ),
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Insta.profile'),
        ),
    ]
