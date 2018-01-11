from flask import Blueprint, render_template

blueprint = Blueprint(
    'UI_elements_blueprint', 
    __name__, 
    url_prefix = '/UI_elements', 
    template_folder = 'templates',
    static_folder = 'static'
    )

@blueprint.route('/<template>')
def route_template(template):
    return render_template(template + '.html')
