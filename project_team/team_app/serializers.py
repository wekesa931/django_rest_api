from rest_framework import serializers
from .models import Teamlist

class TeamlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Teamlist
        fields = ('id','name','specialty','date_posted','date_modified')
        read_only_fields = ('date_created', 'date_modified')