from rest_framework import routers
from .views import QRCodeViewSet

router = routers.DefaultRouter()
router.register(r'generate_qr_code', QRCodeViewSet, basename='generate_qr_code')

urlpatterns = router.urls