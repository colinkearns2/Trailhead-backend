from django.db import models

# Django provides an object relational mapping (ORM)
# allows us to write python code to create database models and 
# then those models are AUTOMATICALLY created for us in SQL light 3 
# we make a migration, which is automated code, which creates the corresponding model in SQL or mongoDB

class TodoItem(models.Model): 
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
