from rest_framework import serializers
from people.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'age',
        )
        model = Person
