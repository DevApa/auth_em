from rest_framework.routers import DefaultRouter

from register.views import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuario', UsuarioViewSet, basename='usuario')

urlpatterns = router.urls
