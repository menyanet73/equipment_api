from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from users.views import TokenCreateView, UserViewset
from equipment.views import EquipmentView, EquipmentTypeView


router = SimpleRouter()
router.register(r'equipment', EquipmentView, basename='equipment')
router.register(r'equipment-type', EquipmentTypeView, basename='equipment-type')
router.register(r'user/create', UserViewset, basename='users')
router.register(r'user/login', TokenCreateView, basename='login')

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
