from django.db import models
from django.contrib.auth.models import User
from clients.models import Client

class Note(models.Model):
    NOTE_TYPES = [
        ('call', 'Call'),
        ('meeting', 'Meeting'),
        ('idea', 'Idea'),
        ('contract', 'Contract'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='notes')

    title = models.CharField(max_length=255, blank=True, default="Untitled")
    content = models.TextField(blank=True)
    type = models.CharField(max_length=20, choices=NOTE_TYPES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title