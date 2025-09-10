from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from .permissions import IsAuthorOrRead
from .models import Incidents
from .serializers import AttacksSerializer, UpdateAttack

import json

class AllAttacks(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AttacksSerializer

    def get_queryset(self):
        filter_status = self.request.GET.get('status_filter')
        filter_attack = self.request.GET.get('attack_filter')
        query = Incidents.objects.all()
        print(filter_attack, filter_status)

        try:
            if filter_status != 'all':
                query = query.filter(Status__status = filter_status)
            if filter_attack != 'all':
                query = query.filter(Attack__attack_name = filter_attack)
        except:
            return Incidents.objects.none()
        return query

class CreateNote(ListCreateAPIView):
    queryset = Incidents.objects.all()
    serializer_class = AttacksSerializer

class UpdateDeleteNote(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrRead, )
    queryset = Incidents.objects.all()
    serializer_class = UpdateAttack