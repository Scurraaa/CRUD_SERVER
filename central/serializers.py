from rest_framework import serializers
from . import models


class StudentSerializers(serializers.ModelSerializer):

    class Meta:
        fields = ('student_number', 'first_name', 'middle_initial', 'last_name', 'year_level', 'program','password')
        model = models.Student
