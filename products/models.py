from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    Title       = models.CharField(max_length=120)
    Description = models.TextField(blank=True, null=True)
    Price       = models.DecimalField(decimal_places=2, max_digits=1000)
    Summary     = models.TextField(blank=True, null=True)
    Featured    = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     return f"/products/{self.id}/"

    def get_absolute_url(self):
        return reverse("products:product_dynamic", kwargs={"my_id": self.id})#f"/products/{self.id}/"