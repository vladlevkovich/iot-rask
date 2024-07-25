from middlewares.auth_middleware import user_auth_middleware
from logging import getLogger, basicConfig, DEBUG
from models.models import db
from services.user_services import *
from services.device_services import *

logger = getLogger()
FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'
basicConfig(level=DEBUG, format=FORMAT)


async def main():
    app = web.Application(middlewares=[user_auth_middleware])
    app.router.add_post('/register', register)
    app.router.add_post('/login', login)
    app.router.add_post('/add', add_device)
    app.router.add_get('/device/{device_id}', get_device)
    app.router.add_put('/device-update/{device_id}', update_device)
    app.router.add_delete('/device-delete/{device_id}', delete_device)
    return app


if __name__ == '__main__':
    logger.info('START SERVER')
    application = main()
    db.create_tables([User, Location, Device])
    web.run_app(application, port=8000)
