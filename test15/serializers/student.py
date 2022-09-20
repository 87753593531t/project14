from rest_framework.serializers import ModelSerializer

from test15.models import Student


class StudentSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = (
            'id',
            'name',
            'surname',
            'city'
        )
