from app import create_app, db
from app.base.models import User
from flask_migrate import Migrate

app = create_app()
Migrate(app, db)