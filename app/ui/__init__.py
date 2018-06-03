from flask import Blueprint

blueprint = Blueprint(
    'ui_blueprint',
    __name__,
    url_prefix='/ui',
    template_folder='templates',
    static_folder='static'
)
