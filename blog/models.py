from django.db import models
import datetime 

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(default=datetime.date.today)

    class Meta:
        verbose_name = "Trabajo"
        verbose_name_plural = "Trabajos"

    def __str__(self) -> str:
        return self.title
