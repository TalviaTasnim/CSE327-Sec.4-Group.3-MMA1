from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.TextField()
    def __str__(self):
         return self.name
     
     

class Question(models.Model):
    question = models.CharField(max_length=300)
    answered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    votesscore = models.IntegerField(default='0')
    amountofvotes = models.IntegerField(default='0')

    def __str__(self):
        return self.question


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, blank=False, null=True)
    answer = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer