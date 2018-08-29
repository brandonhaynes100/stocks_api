from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow, ALL_PERMISSIONS


class RootACL:
    __acl__ = [
        (Allow, 'admin', ALL_PERMISSIONS),
        (Allow, 'view', ['read']),
    ]

    def __init__(self, request):
        pass


def add_role_principal(userid, request):
    return request.jwt_claims.get('roles', [])


# this function is the entry point to the application. It is called when pserve is run
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # for debugging
    # import pdb; pdb.set_trace()

    # setting up
    config = Configurator(settings=settings)
    # when you pass a module using include() , it needs an includeme(config) function
    config.include('pyramid_jwt')
    config.include('pyramid_restful')

    config.set_root_factory(RootACL)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.set_jwt_authentication_policy(
        'superseekretseekrit',  # os.environ.get('SECRET', None)
        auth_type='Bearer',
        callback=add_role_principal,
    )

    config.include('.models')
    config.include('.routes')
    # looks for any @view_config decorators, then will register at a view controller
    config.scan()

    # this is an HTTP server (Web Server Gateway Interface) - a form of server application
    return config.make_wsgi_app()
