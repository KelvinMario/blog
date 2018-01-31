from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:20]
