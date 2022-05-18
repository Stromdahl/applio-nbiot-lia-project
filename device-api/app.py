from sqlalchemy.exc import SQLAlchemyError
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)


class nbdevices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(80), unique=True, nullable=False)
    application_name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, device_name, application_name):
        self.device_name = device_name
        self.application_name = application_name


db.create_all()


@app.route('/devices/<device_name>', methods=['GET'])
def get_device(device_name):
    device = nbdevices.query.filter_by(device_name=device_name).first()
    if not device:
        return f"Device with device name: {device_name} does not exist", 404
    del device.__dict__['_sa_instance_state']
    return device.__dict__


@app.route('/devices/<device_name>', methods=['DELETE'])
def delete_device(device_name):
    name_of_device = nbdevices.query.filter_by(device_name=device_name).first()
    if not name_of_device:
        return f'Unfortunately can not delete device with device name: {device_name}. It does not exist', 404
    else:
        db.session.query(nbdevices).filter_by(device_name=device_name).delete()
        db.session.commit()
        return f' Deleted device with device name: {device_name}'


@app.route('/devices/', methods=['POST'])
def create_device():
    try:
        body = request.get_json()
        db.session.add(nbdevices(body['device_name'], body['application_name']))
        db.session.commit()
        return body
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return error, 422


@app.route('/devices', methods=['GET'])
def get_devices():
    devices = []
    for device in db.session.query(nbdevices).all():
        del device.__dict__['_sa_instance_state']
        devices.append(device.__dict__)
    return jsonify(devices)