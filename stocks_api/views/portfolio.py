# TODO
from ..models.schemas import PortfolioSchema
from ..models import Account
from ..models import Portfolio
from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError, DataError
from pyramid.response import Response
from pyramid.view import view_config
import requests
import json
import os


class PortfolioAPIViewset(APIViewSet):
    # POST
    def create(self, request):
        """
        """
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'name' not in kwargs:
            return Response(json='Expected value; name', status=400)

        # This is new, and required for managing model relationships
        if request.authenticated_userid:
            account = Account.one(request, request.authenticated_userid)
            kwargs['account_id'] = account.id

        try:
            portfolio = Portfolio.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate Key Error. Name already exists.', status=409)

        schema = PortfolioSchema()
        data = schema.dump(portfolio).data

        return Response(json=data, status=201)
        # return Response(
        #     json={'message': 'Created a new resource.'},
        #     status=201
        # )

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

    # DELETE
    def destroy(self, request, id=None):
        """
        """
        if not id:
            return Response(json='Not Found', status=404)

        try:
            Portfolio.remove(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        return Response(status=204)
