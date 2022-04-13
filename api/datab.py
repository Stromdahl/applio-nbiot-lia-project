from api.app import nbdevices, db


def add_device(device_name, application_name):
    db.session.add(nbdevices(device_name,application_name))
    db.session.commit()

