from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from trunkjunk2api.models import BandanaCollection


class BandanaCollectionView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single bandana_collection"""
        try:
            bandanacollection = BandanaCollection.objects.get(pk=pk)
            serializer = BandanaCollectionSerializer(bandanacollection)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """GET all bandana_collections"""
        bandanacollections = BandanaCollection.objects.all()
        serializer = BandanaCollectionSerializer(bandanacollections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        """Handle Delete requests for a bandana_collections"""
        bandanacollection = BandanaCollection.objects.get(pk=pk)
        bandanacollection.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class BandanaCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandanaCollection
        fields = ('id', 'bandana', 'collection')
        depth = 2
    