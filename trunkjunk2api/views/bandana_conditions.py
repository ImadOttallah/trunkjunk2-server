from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from trunkjunk2api.models import BandanaCondition


class BandanaConditionView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single collection"""
        try:
            bandana_condition = BandanaCondition.objects.get(pk=pk)
            serializer = BandanaConditonSerializer(bandana_condition)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """GET all bandana colors"""
        bandana_condition = BandanaCondition.objects.all()
        serializer = BandanaConditonSerializer(bandana_condition, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle PUT requests for a bandana color"""
        bandana_condition = BandanaCondition.objects.create(
            name = request.data["name"],
        )
        serializer = BandanaConditonSerializer(bandana_condition)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a bandana color"""
        bandana_condition = BandanaCondition.objects.get(pk=pk)
        bandana_condition.name = request.data["name"]
        bandana_condition.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle Delete requests for a collection"""
        bandana_condition = BandanaCondition.objects.get(pk=pk)
        bandana_condition.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class BandanaConditonSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandanaCondition
        fields = ('name', 'id')
        depth = 2
    