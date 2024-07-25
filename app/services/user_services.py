from aiohttp import web
from logging import getLogger
from app.models.models import User
from app.secruity.secruity import hash_password, check_password
from .auth import auth


logger = getLogger(__name__)


async def register(request):
    try:
        data = await request.json()
        name = data['name']
        email = data['email']
        password = data['password']

        if not all([name, email, password]):
            logger.info('Missing fields')
            return web.Response(text='Missing fields', status=400)

        hashed_password = hash_password(password)

        user = User(
            name=name,
            email=email,
            password=hashed_password
        )
        user.save()
        logger.info('User registration was successful')
        return web.json_response({
            'id': user.id,
            'email': user.email,
            'name': user.name
        })
    except Exception as e:
        logger.debug(str(e))
        return web.Response(text=str(e), status=500)


async def login(request):
    try:
        data = await request.json()
        user = User.get(email=data['email'])

        if not user:
            logger.info('User not found')
            return web.Response(text='User not found', status=404)

        if not check_password(user.password, data['password']):
            logger.info('Invalid data')
            return web.Response(text='Invalid data', status=400)

        access_token = auth.create_access_token({'id': user.id, 'email': user.email})
        logger.info('User login was successful')
        return web.json_response({'access_token': access_token})
    except Exception as e:
        logger.debug(str(e))
        return web.Response(text=str(e), status=500)
