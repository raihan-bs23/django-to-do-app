from django.db import models


# Create your models here.
class TodoList(models.Model):
    id = models.AutoField(primary_key=True)
    timestamps = models.DateTimeField(auto_now_add=True)
    todo_name = models.CharField(max_length=4000)
    is_completed = models.CharField(max_length=50)

    class Meta:
        db_table = 'todo_app'
