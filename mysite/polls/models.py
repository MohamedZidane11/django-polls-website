from django.db import models

# Question:-
# question_text = ""
# publish_date = ""
#
# # Choices:-
# choice_text = ""
# number_of_votes = ""
# link = ""

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    number_of_votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.choice_text


