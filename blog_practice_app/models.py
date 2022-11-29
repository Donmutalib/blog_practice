from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title








