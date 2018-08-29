
# TODO
from ..models.schemas import WeatherLocationSchema
from ..models import WeatherLocation

from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError, DataError
from pyramid.response import Response
from pyramid.view import view_config
import requests
import json
import os



class NameLookupAPIView(APIViewSet):
    def retrieve(self, request, name):
        """
        """
        # TODO
        url = ''.format(
            request.matchdict['name'],
            # TODO
            ''
        )
        response = requests.get(url)


class CompanyAPIViewset(APIViewSet):
    def retrieve(self, request, id):
        # http :6543/api/v1/company/{id}/

        # Use the 'id' to lookup that resource in the DB,
        # Formulate a response and send it back to the client
        return Response(
            json={'message': 'Provided a single resource'},
            status=200
        )


    # an example
    # def list(self, request):
    #     http :6543/api/v1/company/
    #     pass
