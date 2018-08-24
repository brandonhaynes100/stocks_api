from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class StocksAPIViewset(APIViewSet):


    # GET all
    def list(self, request):
        return Response(
            json={'message': 'Provided a list of stocks.'},
            status=200)

    # GET one
    def retrieve(self, request):
        return Response(
            json={'message': 'Listing one of the records.'},
            status=200)

    # POST
    def create(self, request):
        return Response(
            json={'message': f'Created a new resource'},
            status=201
            )

    # DELETE
    def destroy(self, request, id):
        return Response(json={'message': 'Deleted the record.'}, status=204)
