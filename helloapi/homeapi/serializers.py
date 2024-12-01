from rest_framework import serializers
from .models import ItemsData

class ItemSerializerData(serializers.ModelSerializer):
    class Meta:
        model = ItemsData
        fields = "__all__"
