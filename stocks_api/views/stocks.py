from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response

# TODO: Where does this go? (It's a view, not a model)
# class SymbolLookupAPIView(APIViewSet):
#     def retrieve(self, request, symbol):
#         """
#         """
#         # TODO
#         url = ''.format(
#             request.matchdict['symbol'],
#             # TODO
#             ''
#         )
#         response = requests.get(url)


class StockAPIViewset(APIViewSet):
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
