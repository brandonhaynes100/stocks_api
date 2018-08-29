# TODO
# from ..models.schemas import WeatherLocationSchema
# from ..models import WeatherLocation
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


class PortfolioAPIViewset(APIViewSet):
    # GET one
    def retrieve(self, request, id):
        return Response(
            json={'message': 'Provided a single resource.'},
            status=200
        )

    # GET all
    def list(self, request):
        return Response(
            json={'message': 'Provided a list of stocks.'},
            status=200
        )

    # POST
    def create(self, request):
        return Response(
            json={'message': 'Created a new resource.'},
            status=201
        )

    # DELETE
    def destroy(self, request, id):
        return Response(status=204)
