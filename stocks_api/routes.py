from pyramid_restful.routers import ViewSetRouter
from .views.stocks import StocksAPIView
# from .views.auth import AuthAPIView


# ties class definition to routes
def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    router = ViewSetRouter(config)

    # path/endpoint, class we just defined/viewset, alias/routename
    router.register('api/vq/stocks', StocksAPIView, 'stocks')
    # router.register('api/v1/auth', AuthAPIView, 'auth')
