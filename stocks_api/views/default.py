from pyramid.response import Response
from pyramid.view import view_config
# no itellisense for above means problem with virtual env,


# configure a function that represents our homeroute, defined as forward slash
# responsible for receiving a request, building a response, returning that response?
@view_config(route_name='home', renderer='json', request_method='GET')
def home_view(request):
    """
    """
    # message should be a list of how to interact with API
    message = '''
        GET / - Base API route\n
        POST /api/v1/auth/ - Register a new account\n
        GET /api/v1/auth/ - Login to an existing account\n
        GET /api/v1/weather/ - Retrieve all weather information\n
        GET /api/v1/weather/<int>/ - Retrieve specific weather record\n
        POST /api/v1/weather/ - Create new weather record\n
        DELETE /api/v1/weather/<int>/ - Remove existing weather record\n '''
    return Response(body=message, status=200)

# define type of renderer


# what type of request methods can operate on this


# define a response
