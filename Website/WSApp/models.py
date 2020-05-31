from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    files = models.FileField(upload_to="storage/%Y/%m/", blank=True)

    def __str__(self):
        return self.title
