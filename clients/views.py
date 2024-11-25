from rest_framework.viewsets import ModelViewSet
from .models import Client
from .serializers import ClientSerializer

# Create your views here.


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
