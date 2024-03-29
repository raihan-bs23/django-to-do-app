# Generated by Django 4.1.7 on 2023-03-30 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamps', models.DateTimeField(auto_now_add=True)),
                ('todo_name', models.CharField(max_length=4000)),
                ('is_completed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'todo_app',
            },
        ),
    ]
