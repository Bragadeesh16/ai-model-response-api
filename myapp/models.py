from django.db import models

class AiResponse(models.Model):
    prompt = models.TextField()
    response_text = models.TextField()
    model_used = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    processing_time = models.FloatField()