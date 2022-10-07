import connexion
import os
from flask_migrate import Migrate
from api.utils.config import load_config
from api.models import db, init_db_session


def create_app():
    connex_app = connexion.App(__name__, specification_dir='api/swagger/')
    connex_app.add_api('root.yaml')
    app = connex_app.app

    app.config.update(load_config())
    database_init(app)
    return app


def database_init(app):
    POSTGRES = {
        'user': app.config["USER"],
        'pw': app.config["PW"],
        'db': app.config["DB"],
        'host': app.config["HOST"],
        'port': app.config["PORT"]
    }
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        os.getenv("SQLALCHEMY_DATABASE_URI",
                  'postgresql://%(user)s:%(pw)s@'
                  '%(host)s:%(port)s/%(db)s' % POSTGRES)
    init_db_session(db.session)
    with app.app_context():
        import api.models as models
        Migrate(app, db)
        models.load()
        db.init_app(app)
        db.create_all(app=app)
