# Generated by Django 3.2.3 on 2021-05-22 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Insta', '0016_auto_20210522_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='comments',
            field=models.CharField(blank=True, max_length=2200),
        ),
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Insta.profile'),
        ),
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posted_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
