from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import ValidationError

from test15.models import Student
from test15.serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all().order_by('id')


class StudentViewSet2(APIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs.keys():
            serializer = self.serializer_class(Student.objects.filter(pk=kwargs['id']).first())
        else:
            serializer = self.serializer_class(Student.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):

        if 'id' in kwargs.keys():
            try:
                s1 = Student.objects.get(id=kwargs['id'])
                serializer = self.serializer_class(s1)
                serializer.update(s1, request.data)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            except:
                raise ValidationError("couldn't find object by id")
        else:
            raise ValidationError("not given student's id")

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        if 'id' in kwargs.keys():
            s1 = Student.objects.get(id=kwargs['id'])
            try:
                s1.delete()
            except:
                raise ValidationError("couldn't find object by id")
        else:
            raise ValidationError('not sent id')
        return Response(data={"details": "object deleted!"}, status=status.HTTP_200_OK)
