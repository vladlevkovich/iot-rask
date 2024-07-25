from app.models.models import *


def test_location(test_db):
    location = Location.create(name='Ukraine')
    assert location.id is not None
    assert location.name == 'Ukraine'


def test_device(test_db):
    user = User.create(name='test user', email='testemail@gmail.com', password='password123')
    location = Location.create(name='Ukraine')
    device = Device.create(
        name='Device1',
        type='sensor',
        login='device_login',
        password='device_password',
        location=location,
        user=user
    )
    assert device.id is not None
    assert device.name == 'Device1'
    assert device.type == 'sensor'
    assert device.login == 'device_login'
    assert device.location.name == 'Ukraine'
    assert device.user.name == 'test user'


def test_get_device(test_db):
    user = User.create(name='test user', email='testemail@gmail.com', password='password123')
    location = Location.create(name='Ukraine')
    Device.create(
        name='Device1',
        type='sensor',
        login='device_login',
        password='device_password',
        location=location,
        user=user
    )
    device_get = Device.get(id=1)
    assert device_get.id == 1
    assert device_get.name == 'Device1'
    assert device_get.type == 'sensor'
    assert device_get.login == 'device_login'
    assert device_get.location.name == 'Ukraine'
    assert device_get.user.name == 'test user'
