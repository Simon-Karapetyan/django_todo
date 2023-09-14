# Generated by Django 4.2.1 on 2023-08-27 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='todo_id',
        ),
        migrations.AddField(
            model_name='todo',
            name='point_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='todo.point'),
            preserve_default=False,
        ),
    ]
