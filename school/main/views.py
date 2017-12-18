from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    CreateAPIView,

)

from main.models import Child, Journal
from main.serializers import (
    ChildSerializer,
    ChildParentsSerializer,
    JournalSerializer
)


class ChildrenView(ListCreateAPIView):
    serializer_class = ChildSerializer
    queryset = Child.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('learn', )


class ChildrenEditInfoView(RetrieveUpdateAPIView):
    serializer_class = ChildSerializer
    queryset = Child.objects.all()


class ChildrenAddParentsView(UpdateAPIView):
    serializer_class = ChildParentsSerializer
    queryset = Child.objects.all()


class JournalAddRecord(CreateAPIView):
    serializer_class = JournalSerializer


class JournalEditRecord(UpdateAPIView):
    serializer_class = JournalSerializer
    queryset = Journal.objects.all()
