from flask import Blueprint

blueprint = Blueprint(
    'tables_blueprint',
    __name__,
    url_prefix='/tables',
    template_folder='templates',
    static_folder='static'
)
