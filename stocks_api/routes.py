from .views import CompanyAPIViewset, StockAPIViewset
from pyramid_restful.routers import ViewSetRouter
from .views.auth import AuthAPIViewset
# from .views.stocks import StocksAPIView
# from .views.auth import AuthAPIView


# ties class definition to routes
def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    router = ViewSetRouter(config)
    # path/endpoint, class we just defined/viewset, alias/routename
    router.register('api/v1/auth/{auth}', AuthAPIViewset, 'auth')
    router.register('api/v1/company', CompanyAPIViewset, 'company')
    router.register('api/v1/stocks', StockAPIViewset, 'stocks')
