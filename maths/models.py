from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


PROBLEMS_SORTABLE_BY = {"time_created", "-time_created", "-time_last_edited", "categories",} #possible ways to query


class Category(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name


class Problem(models.Model):
    question = models.TextField() 
    answer = models.TextField() 
    hint = models.TextField(blank=True)

    timer = models.PositiveIntegerField(blank=True, null=True)
    animation_choices = [(i,i) for i in settings.ANIMATIONS]
    animation = models.FilePathField(path='static/maths/animations', choices=animation_choices, blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name="Problems", blank=True)

    #add an option to add a resource? Not sure exactly how to configure so i'll leave out for now

    user = models.ForeignKey(User, related_name="problems", on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.question


class ProblemSet(models.Model):
    title = models.TextField()
    description = models.TextField(blank = True)
    problems = models.ManyToManyField(Problem, related_name="problem_sets")

    user = models.ForeignKey(User, related_name="problem_sets", on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.title
    





    
    

