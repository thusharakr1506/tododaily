from django.db import models

# Create your models here.

class Task(models.Model):
    task_name=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True,blank=True)
    completion_date=models.DateTimeField(auto_now_add=True,blank=True)

    options=(
        ("completed","completed"),
        ("pending","pending"),
        ("in_progress","in_progress")
    )
    status=models.CharField(max_length=200,choices=options,default="in_progress")

    notify_options=(
        ("daily","daily"),
        ("twice_in_a_day","twice_in_a_day"),
        ("thrice_a_day","thrice_a_day"),
        ("never","never")
    )
    notification=models.CharField(max_length=200,choices=notify_options,default="daily")

    notification_time=models.DateTimeField(auto_now_add=True,blank=True)
    
    user=models.CharField(max_length=200)


    def __int__(self):
        return self.task_name