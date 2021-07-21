from django.db import models

class Reader(models.Model):
    email = models.EmailField(max_length=254)
    opt_out = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
