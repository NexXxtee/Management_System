from django.db import models
from users.models import CustomUser

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField('users.CustomUser', related_name='courses')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']