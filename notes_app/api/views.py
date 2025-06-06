from rest_framework import viewsets
from notes_app.models import Note
from .serializers import NoteSerializer

class ShowNotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer