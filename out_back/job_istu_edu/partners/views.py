from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
    )
from partners.models import Parnter, Practice, DocLink
from partners.serializers import (
    PracticeSerializer,
    PartnerSerializer,
    DocLinkSerializer
    )
# Create your views here.
from django_filters import rest_framework as filters


class PracticeView(ListCreateAPIView):
    queryset = Practice.objects.order_by('id').all()
    serializer_class = PracticeSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['institute']


class PracticeSingleView(RetrieveUpdateDestroyAPIView):
    
    queryset = Practice.objects.order_by('id').all()
    serializer_class = PracticeSerializer
    

class PartnerView(ListCreateAPIView):
    queryset = Parnter.objects.order_by('id').all()
    serializer_class = PartnerSerializer


class PartnerSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Parnter.objects.order_by('id').all()
    serializer_class = PartnerSerializer


class DocLinkView(ListCreateAPIView):
    queryset = DocLink.objects.all()
    serializer_class = DocLinkSerializer


class DocLinkSingleView(RetrieveUpdateDestroyAPIView):
    queryset = DocLink.objects.all()
    serializer_class = DocLinkSerializer