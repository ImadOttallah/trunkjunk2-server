from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from trunkjunk2api.models import BandanaPattern


class BandanaPatternView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single collection"""
        try:
            bandana_pattern = BandanaPattern.objects.get(pk=pk)
            serializer = BandanaPatternSerializer(bandana_pattern)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """GET all bandana patterns"""
        bandana_pattern = BandanaPattern.objects.all()
        serializer = BandanaPatternSerializer(bandana_pattern, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle PUT requests for a bandana pattern"""
        bandana_pattern = BandanaPattern.objects.create(
            name = request.data["name"],
        )
        serializer = BandanaPatternSerializer(bandana_pattern)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a bandana pattern"""
        bandana_pattern = BandanaPattern.objects.get(pk=pk)
        bandana_pattern.name = request.data["name"]
        bandana_pattern.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle Delete requests for a collection"""
        bandana_pattern = BandanaPattern.objects.get(pk=pk)
        bandana_pattern.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class BandanaPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandanaPattern
        fields = ('name', 'id')
        depth = 2
    