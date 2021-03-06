# Generated by Django 3.2.3 on 2021-05-23 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Insta', '0022_auto_20210523_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=2200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_for', to='Insta.image'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commented_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='comments',
            field=models.CharField(blank=True, max_length=2200),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(blank=True, max_length=30),
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
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
