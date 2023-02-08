
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from deshawnapi.models import Walker


class WalkerView(ViewSet):

    def retrieve(self, request, pk=None):
        # Step 1: Get a single walker based on the primary key in the request URL
        walker = Walker.objects.get(pk=pk)

        # Step 2: Serialize the walker record as JSON
        serialized = WalkerSerializer(walker, context={'request': request})

        # Step 3: Send JSON response to client with 200 status code
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        # Step 1: Get all walker data from the database
        cities = Walker.objects.all()

        # Step 2: Convert the data to JSON format
        serialized = WalkerSerializer(cities, many=True)

        # Step 3: Respond to the client with the JSON data and 200 status code
        return Response(serialized.data, status=status.HTTP_200_OK)


class WalkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Walker
        fields = ('id', 'name', 'email', 'city', )

