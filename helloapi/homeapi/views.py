from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ItemsData
from .serializers import ItemSerializerData

class ItemListCreateAPIViewData(APIView):
    def get(self, request):
        items = ItemsData.objects.all()
        serializerdata = ItemSerializerData(items, many=True)
        return Response(serializerdata.data)

    def post(self, request):
        serializerdata = ItemSerializerData(data=request.data)
        if serializerdata.is_valid():
            serializerdata.save()
            return Response(serializerdata.data, status=status.HTTP_201_CREATED)
        return Response(serializerdata.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemDetailAPIViewData(APIView):
    def get_object(self, id):
        try:
            return ItemsData.objects.get(id=id)
        except ItemsData.DoesNotExist:
            return None

    def get(self, request, id):
        item = self.get_object(id)
        if not item:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        serializerdata = ItemSerializerData(item)
        return Response(serializerdata.data)

    def put(self, request, id):
        item = self.get_object(id)
        if not item:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        serializerdata = ItemSerializerData(item, data=request.data)
        if serializerdata.is_valid():
            serializerdata.save()
            return Response(serializerdata.data)
        return Response(serializerdata.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        item = self.get_object(id)
        if not item:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
