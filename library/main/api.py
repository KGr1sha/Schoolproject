from .models import Journal
from rest_framework import viewsets, permissions
from .serializers import JournalSerializer

class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = JournalSerializer