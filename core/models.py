from django.db import models
from users.models import User

class Question(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    faved_by = models.ManyToManyField(User, related_name="q_faves", blank=True)

     
    def __str__(self):
        return f"{self.title} -  {self.author}"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers")  # Is this a problem?
    created = models.DateTimeField(auto_now_add=True)
    faved_by = models.ManyToManyField(User, related_name="a_faves", blank=True)
    body = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Answer to: {self.question.title} by {self.author}"
