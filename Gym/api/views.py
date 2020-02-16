from rest_framework.generics import ListAPIView, RetrieveAPIView
from Gym.models import Sport, Area, Equipment
from .serializers import SportSerializer


class SportListView(ListAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class SportDetailView(RetrieveAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

