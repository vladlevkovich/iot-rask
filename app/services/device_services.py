from aiohttp import web
from logging import getLogger
from app.secruity.secruity import hash_password
from app.models.models import User, Location, Device


logger = getLogger(__name__)


async def add_device(request):
    try:
        data = await request.json()
        name = data['name']
        device_type = data['type']
        device_login = data['login']
        password = data['password']
        device_location = data['location']
        user_id = request['user']['id']
        user_obj = User.get(User.id == user_id)
        location_obj, create = Location.get_or_create(name=device_location)
        device = Device(
            name=name,
            type=device_type,
            login=device_login,
            password=hash_password(password),
            # password=password,
            location=location_obj,
            user=user_obj
        )
        device.save()
        logger.info('Device added successfully')
        return web.json_response({
            'id': device.id,
            'type': device.type,
            'login': device.login,
            'password': device.password,
            'location': device.location.id,
            'user': device.user.id
        })
    except Exception as e:
        logger.debug(str(e))
        return web.Response(text=str(e))


async def get_device(request):
    try:
        device_id = int(request.match_info['device_id'])
        device = Device.get(id=device_id)
        logger.info('Device received successfully')
        return web.json_response({
            'id': device.id,
            'type': device.type,
            'login': device.login,
            'location': device.location.id,
            'user': device.user.id
        })
    except Exception as e:
        logger.debug(str(e))
        return web.Response(text=str(e))


async def update_device(request):
    try:
        device_id = int(request.match_info.get('device_id'))
        user_id = request['user']['id']
        user = User.get(id=user_id)
        device = Device.get(id=device_id)
        if device.user != user:
            logger.info('Device not found')
            return web.json_response({
                'message': 'Device not found'
            })
        data = await request.json()
        if 'name' in data:
            device.name = data['name']
        if 'type' in data:
            device.type = data['type']
        if 'login' in data:
            device.type = data['login']
        if 'password' in data:
            device.password = data['password']
        if 'location' in data:
            location, create = Location.get_or_create(name=data['location'])
            device.location = location
        device.save()
        logger.info('The update was successful')
        return web.json_response({
            'id': device.id,
            'name': device.name,
            'type': device.type,
            'login': device.login,
            'location': device.location.name,
            'user': device.user.id,
        })
    except Device.DoesNotExist:
        logger.debug('Device not found')
        return web.Response(text='Device not found', status=404)
    except Exception as e:
        logger.debug(str(e))
        return web.Response(text=str(e), status=500)


async def delete_device(request):
    try:
        device_id = int(request.match_info.get('device_id'))
        user_id = request['user']['id']
        user = User.get(id=user_id)
        device = Device.get(id=device_id)
        if device.user != user:
            print('!=')
            return web.json_response({
                'message': 'Device not found'
            })
        device.delete_instance()
        return web.json_response({
            'message': 'Device deleted'
        })
    except Device.DoesNotExist:
        print('404')
        return web.Response(text='Device not found', status=404)
    except Exception as e:
        return web.Response(text=str(e), status=500)

