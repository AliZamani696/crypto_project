from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import redis
import json
# Create your models here.



class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crypto_symbol = models.CharField(max_length=10)
    target_price = models.DecimalField(max_digits=20, decimal_places=10)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.crypto_symbol} @ {self.target_price}"


r = redis.Redis(host='localhost', port=6379, db=0)
@receiver(post_save, sender=WatchList)
def update_redis_wathclist(sender, instance, created, **kwargs):
    # if created:
        data = {
            'user_id': instance.user.id,
            'symbol': instance.crypto_symbol.upper(),
            'target_price': float(instance.target_price),
        }
        r.lpush(f"watchlist: {instance.crypto_symbol.upper()}", json.dumps(data))
