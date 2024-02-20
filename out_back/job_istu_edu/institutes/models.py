from django.db import models


class Institute(models.Model):
    
    name = models.TextField()

    
class Speciality(models.Model):

    name = models.TextField()
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='specialities')