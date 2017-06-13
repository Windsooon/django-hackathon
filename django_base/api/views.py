from inner.models import Inner
from inner.serializers import InnerSerializer
from rest_framework import generics


class InnerList(generics.ListCreateAPIView):
    queryset = Inner.objects.all()
    serializer_class = InnerSerializer


class InnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inner.objects.all()
    serializer_class = InnerSerializer
