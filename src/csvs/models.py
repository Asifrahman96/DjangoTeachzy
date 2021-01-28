from django.db import models

# Create your models here.


class Csvs(models.Model):
    file_name = models.FileField(upload_to='csvs/')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "csvs"

    def __str__(self):
        return f"File id:{self.id}"
