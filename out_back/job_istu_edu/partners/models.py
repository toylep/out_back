from django.db import models
from institutes.models import Institute


class Parnter(models.Model):
    name = models.TextField()
    image = models.URLField(max_length=1000)
    agreement = models.TextField()


class Practice(models.Model):

    partner = models.ForeignKey(Parnter, on_delete=models.CASCADE, related_name='practices')
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='practices')


class PracticeTopic(models.Model):
    name = models.TextField()
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE, related_name='practice_topics')


class DocLink(models.Model):
    type = models.TextField()
    url = models.URLField(max_length=1000)
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE, related_name='doc_links')
