import pytest
from aiohttp import web
from app.services.user_services import register, login
from app.secruity.secruity import hash_password, check_password
from app.models.models import User


@pytest.mark.asyncio
async def test_register(test_db, aiohttp_client):
    app = web.Application()
    app.router.add_post('/register', register)
    client = await aiohttp_client(app)

    resp = await client.post('/register', json={
        'name': 'Test user',
        'email': 'testemail@gmail.com',
        'password': 'password123'
    })

    assert resp.status == 200
    data = await resp.json()
    assert data['name'] == 'Test user'
    assert data['email'] == 'testemail@gmail.com'


@pytest.mark.asyncio
async def test_login(test_db, aiohttp_client):
    app = web.Application()
    app.router.add_post('/login', login)
    client = await aiohttp_client(app)
    User.create(name='Test User', email='testemail@gmail.com', password=hash_password('hashed_password'))
    resp = await client.post('/login', json={
        'email': 'testemail@gmail.com',
        'password': 'hashed_password'
    })

    assert resp.status == 200
    data = await resp.json()
    assert 'access_token' in data
