from flask import Blueprint

blueprint = Blueprint(
    'data_blueprint',
    __name__,
    url_prefix='/data',
    template_folder='templates',
    static_folder='static'
)
