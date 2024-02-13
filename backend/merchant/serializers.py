from rest_framework import serializers
from .models import Merchant, Payment, QRCode

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'

class MerchantPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['merchant', 'amount', 'description']
        read_only_fields = ['created_at', 'paid_at', 'buyer']

class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = ['id', 'qr_code_img', 'payment_url', 'created_at','merchant']
