from django.db import models

class WordList(models.Model):
    words = models.CharField(max_length=255)

class Response(models.Model):
    word_list = models.ForeignKey(WordList, on_delete=models.CASCADE)
    response = models.CharField(max_length=255)
    score = models.IntegerField()
