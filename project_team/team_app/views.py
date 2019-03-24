# generics are class based views that
# make reusability of the views
from rest_framework import generics
from .serializers import TeamlistSerializer
from .models import Teamlist

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Teamlist.objects.all()
    serializer_class = TeamlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()