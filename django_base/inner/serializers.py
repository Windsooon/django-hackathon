from .models import Inner
from rest_framework import serializers


class InnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inner
        fields = ("name", "category")
