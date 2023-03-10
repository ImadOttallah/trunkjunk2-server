from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from trunkjunk2api.models import Collection, User, Bandana, BandanaCollection


class CollectionView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single collection"""
        try:
            collection = Collection.objects.get(pk=pk)
            bandanas = Bandana.objects.filter(joined_bandanas__collection_id=collection)
            collection.bandanas.set(bandanas)
            # bandanas = BandanaCollection.objects.filter(collection=collection)
            # collection.bandanas.set(bandanas)
            serializer = CollectionSerializer(collection, context={'collection': collection})
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
class BandanaCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandanaCollection
        fields = ('id',)
class BandanaSerializer(serializers.ModelSerializer):
    """Handle GET request for single collection"""
    joined_bandanas = serializers.SerializerMethodField()
    class Meta:
        model = Bandana
        fields = (
          'id', 
          'name',
          'size',
          'image', 
          'joined_bandanas', 
          'description', 
          'origin', 
          'user',
          'pattern', 
          'marking', 
          'color', 
          'condition')

    def get_joined_bandanas(self, obj):
        """Handle GET request for single collection"""
        collection = self.context.get('collection')
        bandana_collections = obj.joined_bandanas.filter(collection=collection)
        serializer = BandanaCollectionSerializer(bandana_collections, many=True)
        return serializer.data
class CollectionSerializer(serializers.ModelSerializer):
    bandanas=BandanaSerializer(many=True)
    class Meta:
        model = Collection
        fields = ('id', 'user', 'name', 'image', 'description','bandanas')
        depth = 2
