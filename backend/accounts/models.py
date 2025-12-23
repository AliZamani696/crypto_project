from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crypto_symbol = models.CharField(max_length=10)
    target_price = models.DecimalField(max_digits=20, decimal_places=10)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.crypto_symbol} @ {self.target_price}"


