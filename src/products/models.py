from django.db import models
from django.urls import reverse


class Product(models.Model):
    name        = models.CharField(max_length=120) # mapping to the database
    description = models.TextField(
        null=True,  # null refers  data feild in database  False=required
        blank=True, # blank refers data  feild in view  False=required
        default='Comming Soon !'
        )
    price    = models.DecimalField(decimal_places=2, max_digits=100)
    avability = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse(
                        "products:product-details", # 'products:' is the namsespace defiend in ./urls.py
                        kwargs={"product_id": self.id}
                    )
    