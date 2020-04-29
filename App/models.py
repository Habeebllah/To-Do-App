from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.text)

    class Meta:
        verbose_name_plural = 'Todo'