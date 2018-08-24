
from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class CompanyAPIViewset(APIViewSet):
    def retrieve(self, request, id):
        # http :6543/api/v1/company/{id}/
        return Response(json={'message': 'Provided a single resource'})


    # an example
    # def list(self, request):
    #     http :6543/api/v1/company/
    #     pass
