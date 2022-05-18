from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy


def init_db(app):
    global db
    db = SQLAlchemy(app)

# Hello

class nbdevices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(80), unique=True, nullable=False)
    application_name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, device_name, application_name):
        self.device_name = device_name
        self.application_name = application_name


db.create_all()


def read_device(id):
    device = nbdevices.query.get(id)
    del device.__dict__['_sa_instance_state']
    return device


def create_device(device_name, application_name):
    db.session.add(nbdevices(device_name, application_name))
    db.session.commit()
