from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from equipment.views import EquipmentView, EquipmentTypeView


router = SimpleRouter()
router.register(r'equipment', EquipmentView, basename='equipment')
router.register(r'equipment-type', EquipmentTypeView, basename='equipment-type')

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
