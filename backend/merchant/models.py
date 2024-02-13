from django.db import models
from buyer.models import Buyer

class Merchant(models.Model):
    name = models.CharField(max_length=100)
    

class Payment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    buyer = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True, blank=True)

class QRCode(models.Model):
    qr_code_img = models.TextField()
    payment_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)