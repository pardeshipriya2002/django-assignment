from django.db import models

# Create your models here.   
Type = [
    ('Pending','Pending'),
    ('Done','Done')
]
class Task(models.Model):
    Task_Details = models.CharField(max_length=250)
    Task_Type = models.CharField(max_length=50,choices=Type)
    def __str__(self):
        return str(self.Task_Details)
    
class User(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Mobile = models.IntegerField()
    taskss = models.ForeignKey(Task,on_delete=models.CASCADE,null=True)

    class Meta():
        db_table = 'User'
    def __str__(self):
        return str(self.Name)