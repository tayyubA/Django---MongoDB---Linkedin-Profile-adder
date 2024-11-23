from djongo import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    headline = models.CharField(max_length=200)
    skills = models.JSONField()

    def __str__(self):
        return self.name
