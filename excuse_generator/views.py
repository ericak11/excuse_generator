from pyramid.view import view_config


# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def my_view(request):
#     return {'project': 'excuse_generator'}

@view_config(route_name='home', renderer='home.jinja2')
def my_view(request):
    return {}


@view_config(route_name='no', request_method='POST')
def form(request):
    return {}
