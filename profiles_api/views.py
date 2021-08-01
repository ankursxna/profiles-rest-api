from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
# TokenAuthentication is used for users to authenticate themselves with our API
# It works by generating a random token string when the user logs in and then every request they  make to our API that we need to...
# ...authenticate we add this token string to the request and that's effectively a password to check that every request made is authenticated correctly
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

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

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'Message':'Hello','a_viewset':a_viewset})


    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            age  = serializer.validated_data.get('age')
            message = f'Hello {name} | I have got your age is {age}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handling creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset         = models.UserProfiles.objects.all()

    # Here this is confusing to see that in 'HelloViewSet' there were so many functions defined.
    # Each function for a HTTP method but here we dint define any of them still our API is working fine. How ?
    # Here we have inherited ModelViewSet in this class.
    # This class takes care of all these HTTP Methods as these are very general methods anybody would use.
    # This means in this class all these methods must be defined in this ModelViewSet and hence we wont require to write this code.
    # below we will add permissions and TokenAuthentication -->
    authentication_classes = (TokenAuthentication,)
    permission_classes     = (permissions.UpdateOwnProfile,)
    filter_backends        = (filters.SearchFilter,)
    search_fields          = ('name','email',)
    # Similar to what I commented in serializer.py file about keywords, I thought that 'filter_backends' and ...
    # ...'search_fields' are also keywords. Hence I did a quick experiment by jus tweaking the filter_backends to filter_ackens...
    # ... and 'search_fields' to 'search'. Closed the server and started again. and Yes the filter widget was gone.
    # Then I first corrected back 'filter_backends' but stop-start the server which dint add the filter widget.
    # Then I corrected back the 'search_fields' and then stop-start the server which worked and widget was back.


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
