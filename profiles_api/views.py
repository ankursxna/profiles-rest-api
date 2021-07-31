from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

# As per udemy trainer the status object from the rest framework is a list of handy ...
# ... HTTP status codes that you can use when returning responses from your API

class HelloAPIView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer
    # This means when this class or technically when this webpage is called, this serializer ...
    # ... will be automatically called.
    # So very similar to text widget in tkinter which we can set at some place while calling the class so that it is called with the GUI.
    # Downwards we are going to get the input value from this field created which we compare with Tkinter 'get' methods we use ...
    # ... to get input value from GUI.

    def get(self, reuest, format=None):
        """Returns a list of APIView Features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello Ankur','an_apiview':an_apiview})

        # Django REST API is expecting a Response object. Hence we are returning a Response object here.
        # Response object is converted into JSON. As we know JSON file format is Key-Value pair means a dictonary format.
        # Hence inside the Response, we are passing values in the form of dictonary.

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        # What is happening here is what I mentioned above that we need to get the inserted data from our widget.
        # But how are we inserting a paramter'(data=request.data)' into serializer_class is because ...
        # ... in serializers.py file we cerated 'HelloSerializer' class and inherited the 'serializers.Serializer' into it.
        # Next we will validate the input data based on the conditions we set. Like here we set condition of having max_length=10

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            age  = serializer.validated_data.get('age')
            message = f'Hello {name} | I have got your age is {age}'
            return Response({'Message':message})

        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'Message':'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'Message':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'Message':'DELETE'})
