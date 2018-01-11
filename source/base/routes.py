from flask import Blueprint, render_template

blueprint = Blueprint(
    'base_blueprint', 
    __name__, 
    url_prefix = '/base', 
    template_folder = 'templates',
    static_folder = 'static'
    )

@blueprint.route('/<template>')
def route_template(template):
    return render_template(template)

## Errors

@app.errorhandler(403)
def not_found_error(error):
    return render_template('page_403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('page_404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('page_500.html'), 500