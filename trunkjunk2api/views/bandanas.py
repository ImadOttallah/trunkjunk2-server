from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from trunkjunk2api.models import Bandana, User, BandanaPattern, BandanaMarking, BandanaColor, BandanaCondition


class BandanaView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET request for single collection"""
        try:
            bandana = Bandana.objects.get(pk=pk)
            serializer = BandanaSerializer(bandana)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """GET all campaigns"""
        bandanas = Bandana.objects.all()
        serializer = BandanaSerializer(bandanas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle PUT requests for a campaign"""
        user = User.objects.get(pk=request.data["user"])
        pattern = BandanaPattern.objects.get(pk=request.data["pattern"])
        marking = BandanaMarking.objects.get(pk=request.data["marking"])
        color = BandanaColor.objects.get(pk=request.data["color"])
        condition = BandanaCondition.objects.get(pk=request.data["condition"])
        bandana = Bandana.objects.create(
            name = request.data["name"],
            size = request.data["size"],
            image = request.data["image"],
            description = request.data["description"],
            origin = request.data["image"],
            pattern = pattern,
            marking = marking,
            color = color,
            condition = condition,
            user=user,

        )
        serializer = BandanaSerializer(bandana)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a campaign"""
        pattern = BandanaPattern.objects.get(pk=request.data["pattern"])
        marking = BandanaMarking.objects.get(pk=request.data["marking"])
        color = BandanaColor.objects.get(pk=request.data["color"])
        condition = BandanaCondition.objects.get(pk=request.data["condition"])
        
        bandana = Bandana.objects.get(pk=pk)
        bandana.name = request.data["name"]
        bandana.image = request.data["image"]
        bandana.description = request.data["description"]
        bandana.pattern = pattern
        bandana.marking = marking
        bandana.color = color
        bandana.condition = condition
        
        bandana.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle Delete requests for a collection"""
        bandana = Bandana.objects.get(pk=pk)
        bandana.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class BandanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bandana
        fields = ('id', 'user', 'name', 'size','image', 'description', 'origin','pattern','marking','color','condition')
        depth = 2
    