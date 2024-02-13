from rest_framework import serializers
from merchant.models import Payment, Merchant

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ['name']

class PaymentSerializer(serializers.ModelSerializer):
    merchant = MerchantSerializer()

    class Meta:
        model = Payment
        fields = ['id', 'merchant', 'amount', 'description', 'created_at', 'paid_at', 'status', 'buyer']
