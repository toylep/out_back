from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
    )
from institutes.models import Institute, Speciality
from institutes.serializers import InstituteSerializer, SpecialitySerializer
# Create your views here.


class SpecialityView(ListCreateAPIView):

    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class SpecialitySingleView(RetrieveUpdateDestroyAPIView):

    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class InstituteView(ListCreateAPIView):

    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer


class InstituteSingleView(RetrieveUpdateDestroyAPIView):

    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer