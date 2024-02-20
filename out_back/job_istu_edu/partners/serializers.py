from rest_framework.serializers import ModelSerializer
from partners.models import Parnter, Practice, DocLink, PracticeTopic


class DocLinkSerializer(ModelSerializer):

    class Meta:
        model = DocLink
        fields = '__all__'


class PartnerSerializer(ModelSerializer):

    class Meta:
        model = Parnter
        fields = '__all__'


class PracticeTopicSerializer(ModelSerializer):

    class Meta:
        model = PracticeTopic
        fields = '__all__'


class PracticeSerializer(ModelSerializer):
    doc_links = DocLinkSerializer(many=True, read_only=True)
    partner = PartnerSerializer(read_only=True)
    practice_topics = PracticeTopicSerializer(many=True, read_only=True)

    class Meta:
        model = Practice
        fields = '__all__'
