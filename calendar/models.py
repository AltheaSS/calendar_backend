from django.db import models

# Create your models here.


# class Question(models.Model):
#     def __str__(self):
#         return self.question_text
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")


# class Choice(models.Model):
#     def __str__(self):
#         return self.choice_text
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)




class Date(models.Model): #A new date with event and task
    def __str__(self):
        return self.date
    date = models.DateField(unique = True)


class Event(models.Model): #A new event
    def __str__(self):
        return f"{self.date}: {self.description}"
    date = models.ForeignKey(Date, on_delete = models.CASCADE, related_name = "events")
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.CharField(max_length = 200)

# class Task(models.Model): #A new task, a task has priority and length
#     date = models.ForeignKey(Date, on_delete = models.CASCADE, related_name = "tasks")
#     length = models.IntegerField(default = 30) #minutez
#     priority = models.IntegerField(default=1)


