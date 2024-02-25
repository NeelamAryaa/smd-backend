# Generated by Django 5.0 on 2024-02-25 10:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='postanalytics',
            name='content',
            field=models.TextField(default='hi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postanalytics',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postanalytics',
            name='description',
            field=models.TextField(default='des', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postanalytics',
            name='title',
            field=models.CharField(default='title', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='upcomingpost',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]