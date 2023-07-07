from django.db import models
from django.urls import reverse

class Blogs(models.Model):
    topic  = models.CharField(max_length=120)
    post   = models.CharField(max_length=250)  
    online = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("Blogs:detail-post", kwargs={"id": self.id})
    
