from aiohttp.web_middlewares import middleware
from aiohttp.web_exceptions import HTTPUnauthorized
import jwt


@middleware
async def user_auth_middleware(request, handler):
    if request.path in ['/register', '/login']:
        # ендпоінти для яких не потріібен токен
        return await handler(request)
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        raise HTTPUnauthorized(reason="Missing authorization header")
    try:
        token = auth_header.split(' ')[-1]
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        request['user'] = payload
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        raise HTTPUnauthorized(reason='Invalid token')

    response = await handler(request)
    return response
