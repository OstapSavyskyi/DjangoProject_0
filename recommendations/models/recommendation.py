from django.db import models

# Create your models here.


class Recommendation(models.Model):
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    recommended_products = models.ManyToManyField('products.Product')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recommendations for {self.client.name}"
