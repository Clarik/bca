from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    actice = models.BooleanField(default=True)

    def get_absolute_url(self):
        None
        #return reverse(":", kwargs={"my_id": self.id})
