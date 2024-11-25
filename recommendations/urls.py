from rest_framework.routers import DefaultRouter
from .views import RecommendationViewSet

router = DefaultRouter()
router.register(r'', RecommendationViewSet, basename='recommendations')

urlpatterns = router.urls
