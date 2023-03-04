from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from trunkjunk2api.models import BandanaColor


class BandanaColorView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single collection"""
        try:
            bandana_color = BandanaColor.objects.get(pk=pk)
            serializer = BandanaColorSerializer(bandana_color)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """GET all bandana colors"""
        bandanas = BandanaColor.objects.all()
        serializer = BandanaColorSerializer(bandanas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle PUT requests for a bandana color"""
        bandana_color = BandanaColor.objects.create(
            name = request.data["name"],
        )
        serializer = BandanaColorSerializer(bandana_color)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a bandana color"""
        bandana_color = BandanaColor.objects.get(pk=pk)
        bandana_color.name = request.data["name"]
        bandana_color.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle Delete requests for a collection"""
        bandana_color = BandanaColor.objects.get(pk=pk)
        bandana_color.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class BandanaColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandanaColor
        fields = ('name', 'id')
        depth = 2
    