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
    message = 'Hello world'
    return Response(body=message, content_type='text/plain', status=200)

# define type of renderer


# what type of request methods can operate on this


# define a response
