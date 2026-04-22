from django.db import models

class Conversation(models.Model):
    role = models.CharField(max_length=10)   # user / assistant
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)