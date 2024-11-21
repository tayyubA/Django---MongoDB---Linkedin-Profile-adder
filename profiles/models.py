from djongo import models  # Import models from djongo

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    headline = models.CharField(max_length=200)
    skills = models.JSONField()  # JSONField from Djongo to store skills

    def __str__(self):
        return self.name
