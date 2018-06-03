from flask import Blueprint

blueprint = Blueprint(
    'forms_blueprint',
    __name__,
    url_prefix='/forms',
    template_folder='templates',
    static_folder='static'
)
