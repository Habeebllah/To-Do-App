from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=500)
    added_date_time = models.DateTimeField()

    def __str__(self):
        return (self.text)

    class Meta:
        verbose_name_plural = 'Todo'