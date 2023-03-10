# Generated by Django 4.1.3 on 2022-12-10 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=150)),
                ('resim', models.FileField(upload_to='postlar/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dislike', models.ManyToManyField(related_name='dislike', to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('retweet', models.ManyToManyField(related_name='retweet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
