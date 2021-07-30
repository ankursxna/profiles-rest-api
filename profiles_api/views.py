from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""

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
