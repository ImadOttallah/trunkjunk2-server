from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from trunkjunk2api.models import BandanaMarking


class BandanaMarkingView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single collection"""
        try:
            bandana_marking = BandanaMarking.objects.get(pk=pk)
            serializer = BandanaConditionSerializer(bandana_marking)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """GET all bandana colors"""
        bandana_marking = BandanaMarking.objects.all()
        serializer = BandanaConditionSerializer(bandana_marking, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle PUT requests for a bandana color"""
        bandana_marking = BandanaMarking.objects.create(
            name = request.data["name"],
        )
        serializer = BandanaConditionSerializer(bandana_marking)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a bandana color"""
        bandana_marking = BandanaMarking.objects.get(pk=pk)
        bandana_marking.name = request.data["name"]
        bandana_marking.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle Delete requests for a collection"""
        bandana_marking = BandanaMarking.objects.get(pk=pk)
        bandana_marking.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class BandanaConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandanaMarking
        fields = ('name', 'id')
        depth = 2
    