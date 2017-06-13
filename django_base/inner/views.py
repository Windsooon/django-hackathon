from inner.models import Inner
from inner.serializers import InnerSerializer
from rest_framework import generics


class inner_list(generics.ListCreateAPIView):
    queryset = Inner.objects.all()
    serializer_class = InnerSerializer


class inner_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inner.objects.all()
    serializer_class = InnerSerializer
