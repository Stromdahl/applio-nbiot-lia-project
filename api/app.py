import flask
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


import os

# TODO Om unique id så inte kraschar, utan respons code för att dubblett inte tillåtet.
# TODO Error handling. Va händer om jag gettar något som inte finns etc.

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


# working !
@app.route('/devices/<id>', methods=['GET'])
def get_device(id):
    try:
        device = nbdevices.query.get(id)
        if not device:
            return f"Device with ID: {id} does not exist", 409
        del device.__dict__['_sa_instance_state']
        return jsonify(device.__dict__)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
    return error



# NOT working w error handling http !
@app.route('/devices/<id>', methods=['DELETE'])
def delete_device(id):
    try:
        test = db.session.query(nbdevices).filter_by(id=id)
        if not test:
            return f'Unfortunally can not delete {id} Device with ID: {id} does not exist', 409
        else:
            db.session.query(nbdevices).filter_by(id=id).delete()
            db.session.commit()
            return f' Deleted ID: {id}'

    except SQLAlchemyError as ex:
        error = str(ex.__dict__['orig'])
        return error, 422






# working!
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


'''
@app.route('/devices/', methods=['POST'])
def create_device():
    body = request.get_json()
    add_device(body['device_name'], body['application_name'])
    return body
    //
    db:
    def add_device(device_name, application_name):
    db.session.add(nbdevices(device_name,application_name))
    db.session.commit()
    //

@app.route('/devices/<id>', methods=['DELETE'])
def delete_device(id):
    delete_the_device(id)
    return f"device w. ID {id} deleted"
'''