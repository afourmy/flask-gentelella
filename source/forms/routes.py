from flask import Blueprint, render_template

blueprint = Blueprint(
    'forms_blueprint', 
    __name__, 
    url_prefix = '/forms', 
    template_folder = 'templates',
    static_folder = 'static'
    )

@blueprint.route('/<template>')
def route_template(template):
    return render_template(template + '.html')
