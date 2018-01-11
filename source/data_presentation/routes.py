from flask import Blueprint, render_template

blueprint = Blueprint(
    'data_presentation_blueprint', 
    __name__, 
    url_prefix = '/data_presentation', 
    template_folder = 'templates',
    static_folder = 'static'
    )

@blueprint.route('/<template>')
def route_template(template):
    return render_template(template + '.html')
