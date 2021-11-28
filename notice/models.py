from django.db import models


class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='portfolio/images',blank=True)
    urls = models.URLField(blank=True)
    def __str__(self):
        return self.title