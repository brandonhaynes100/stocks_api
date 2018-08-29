from .views.auth import AuthAPIViewset
from .views.company import CompanyAPIViewset, NameLookupAPIView
from .views.stocks import StockAPIViewset
from .views.portfolio import PortfolioAPIViewset
from pyramid_restful.routers import ViewSetRouter


# ties class definition to routes
def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    # example code
    # config.add_route('lookup', '/api/v1/lookup/{zip}')
    # config.add_route('lookup', '/api/v1/lookup/{name}')

    router = ViewSetRouter(config)
    # example code
    # router.register('api/v1/location', WeatherLocationAPIView, 'location')
    # router.register('api/v1/lookup/{zip_code}', LocationLookupAPIView, 'lookup')

    # path/endpoint, class we just defined/viewset, alias/routename
    router.register('api/v1/company', CompanyAPIViewset, 'company')
    router.register('api/v1/lookup/{name}', NameLookupAPIView, 'lookup')
    router.register('api/v1/stocks', StockAPIViewset, 'stocks')
    router.register('api/v1/portfolio', PortfolioAPIViewset, 'portfolio')
    # NOTE: Discuss permissions on location route and parameter to auth route (optionally add permissions to auth)
    router.register('api/v1/auth/{auth}', AuthAPIViewset, 'auth')
