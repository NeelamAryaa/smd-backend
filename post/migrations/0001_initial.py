

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostAnalytics',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('shares', models.PositiveIntegerField(default=0)),
                ('comments', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=500)),
                ('content', models.TextField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL)),
                ('analytics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics', to='post.postanalytics')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UpcomingPost',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('draft_or_schedule', models.CharField(choices=[('draft', 'Draft'), ('schedule', 'Schedule')], default='draft', max_length=10)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=500)),
                ('content', models.TextField()),
                ('set_time', models.DateField(default=django.utils.timezone.now)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upcoming_post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
