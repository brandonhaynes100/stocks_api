from pyramid.config import Configurator


# this function is the entry point to the application. It is called when pserve is run
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # for debugging
    # import pdb; pdb.set_trace()

    # setting up
    config = Configurator(settings=settings)

    config.include('pyramid_restful')

    # config.include('.models')

    # when you pass a module using include() , it needs an includeme(config) function
    config.include('.routes')

    # looks for any @view_config decorators, then will register at a view controller
    config.scan()

    # this is an HTTP server (Web Server Gateway Interface) - a form of server application
    return config.make_wsgi_app()
