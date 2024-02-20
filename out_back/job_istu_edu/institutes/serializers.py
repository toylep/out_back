from rest_framework.serializers import ModelSerializer
from institutes.models import Institute, Speciality



class SpecialitySerializer(ModelSerializer):

    class Meta:
        model = Speciality
        fields = '__all__'


class InstituteSerializer(ModelSerializer):

    specialities = SpecialitySerializer(many=True, read_only=True)

    class Meta:
        model = Institute
        fields = '__all__'
