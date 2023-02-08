from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from deshawnapi.models import Appointment, Walker


class AppointmentView(ViewSet):
#if we are defining something in the class we call it a 'method' 'defining a method on the class'
#when defining inside a class specifically 
    def retrieve(self, request, pk=None): #declaring a method that accepts the parsed path; a request and a primary key 
        appointment = Appointment.objects.get(pk=pk) #gets a single instance of the Appointment database model class declaring the appoinment variable and assigning to the appointment object that matches PK
        serialized = AppointmentSerializer(appointment, context={'request': request})  #declaring a variable serialized and sets it equal to the return value of the appointment serializer below that will serialize the appointment object we just defined
        return Response(serialized.data, status=status.HTTP_200_OK) #returns a body of json stringified object to the client, and a status code of 200 OK  in the headers
# in a function definition in the parathensis we call those paramaters
    def list(self, request):  #defining a method list with the parameters self, and request 
        #we are declaring the appointments variable and assigning it the value of a list of instances of the Appointment database model 
        #QUERYING the appointment table in the database to return a list of INSTANCES of the database MODEL
        appointments = Appointment.objects.all() 
        serialized = AppointmentSerializer(appointments, many=True) #declaring the serialized variable assigning it to the return JSON string of the appointment serializer which takes the arguments appointments, many=True, which tells the serializer to expect a list of instances 
        return Response(serialized.data, status=status.HTTP_200_OK)
    def create(self, request):
        # Get the related walker from the database using the request body value
        client_walker_id = request.data["walker_id"]
        walker_instance = Walker.objects.get(pk=client_walker_id)

        # Create a new appointment instance
        appointment = Appointment()

        # Use Walker instance as the value of the model property
        appointment.walker = walker_instance

        # Assign the appointment date using the request body value
        appointment.date = request.data["date"]

        # Performs the INSERT statement into the deshawnapi_appontment table
        appointment.save()

        # Serialization will be covered in the next chapter
        serialized = AppointmentSerializer(appointment, many=False)

        # Respond with the newly created appointment in JSON format with a 201 status code
        return Response(serialized.data, status=status.HTTP_201_CREATED)


# The serializer will be covered in the next chapter
class AppointmentSerializer(serializers.ModelSerializer):
#JSON stringifies an object based on the fields we define
    class Meta:
        model = Appointment
        fields = ('id', 'walker', 'date',)  #tuple (tuple, tuple, tuple) <-- looks like this in python (tuple, tuple)
        #why did we define these fields :(  #because we want to return the id, walker, and date of the appointment, that's what the client is expecting
