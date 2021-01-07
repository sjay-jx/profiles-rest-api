from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

    def get(Self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'IS similar to a traditional Django View',
            'Gives you the most control over application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
