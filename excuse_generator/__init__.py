from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('form', '/form', request_method='POST')
    config.scan()
    config.add_jinja2_search_path('templates/')
    return config.make_wsgi_app()
