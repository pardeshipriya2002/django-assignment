from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    mobile = models.IntegerField(verbose_name='Mobile No.')
    userId = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table='User'

    
status=[('Pending','Pending'),('Done','Done')]
class Task(models.Model):
    taskdetail=models.TextField(verbose_name='Detail')
    tasktype=models.CharField(max_length=10,verbose_name='Status', choices=status)
    task_Assign=models.ForeignKey(User, on_delete=models.PROTECT, related_name='tasks')

    def __str__(self):
        return f"{self.task_assign.name} - {self.task_detail[:50]}"
    class Meta:
        db_table='Task'