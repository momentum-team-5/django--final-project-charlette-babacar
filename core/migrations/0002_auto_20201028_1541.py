# Generated by Django 3.1.2 on 2020-10-28 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='body',
            new_name='answer',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='created',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='faved_by',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='is_correct',
        ),
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
        migrations.RemoveField(
            model_name='question',
            name='body',
        ),
        migrations.RemoveField(
            model_name='question',
            name='created',
        ),
        migrations.RemoveField(
            model_name='question',
            name='edited',
        ),
        migrations.RemoveField(
            model_name='question',
            name='faved_by',
        ),
        migrations.RemoveField(
            model_name='question',
            name='title',
        ),
        migrations.AddField(
            model_name='answer',
            name='favoriting_users',
            field=models.ManyToManyField(related_name='favorite_answers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='core.question'),
        ),
    ]
