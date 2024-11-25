from rest_framework.viewsets import ModelViewSet
from .models import Recommendation
from .serializers import RecommendationSerializer
# Create your views here.


class RecommendationViewSet(ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
