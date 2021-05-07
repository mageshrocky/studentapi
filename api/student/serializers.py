from abc import ABC

from rest_framework import serializers
from .models import StudentDetails
from .models import StudentDetails, Subject




class SubjectValidation(serializers.ModelSerializer):
    English = serializers.IntegerField(required=True)
    Maths = serializers.IntegerField(required=True)
    Science = serializers.IntegerField(required=True)
    Optional_subject = serializers.IntegerField(required=True)

    class Meta:
        model = Subject
        fields = ('roll_no', 'English', 'Maths', 'Science', 'Optional_subject')


class StudentValidation(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = '__all__'
