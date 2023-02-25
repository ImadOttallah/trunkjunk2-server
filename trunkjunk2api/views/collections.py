from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from trunkjunk2api.models import Collection, User


class CollectionView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single collection"""
        try:
            collection = Collection.objects.get(pk=pk)
            serializer = CollectionSerializer(collection)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """GET all campaigns"""
        collections = Collection.objects.all()
        bandana = request.query_params.get('bandana', None)
        if bandana is not None:
            bandanas = bandanas.filter(bandana_id=bandana)
            bandana = request.query_params.get('bandana_id', None)
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle PUT requests for a campaign"""
        user = User.objects.get(pk=request.data["user"])
        collection = Collection.objects.create(
            name = request.data["name"],
            image = request.data["image"],
            description = request.data["description"],
            user=user,

        )
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a campaign"""

        collection = Collection.objects.get(pk=pk)
        collection.name = request.data["name"]
        collection.image = request.data["image"]
        collection.description = request.data["description"]
        collection.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle Delete requests for a collection"""
        collection = Collection.objects.get(pk=pk)
        collection.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'user', 'name', 'image', 'description','bandanas')
        depth = 2
    