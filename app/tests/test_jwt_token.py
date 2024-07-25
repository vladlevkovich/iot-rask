from app.services.auth import auth


def test_create_access_token():
    user = {
        'id': 1,
        'email': 'testemail@gmail.com',
    }
    access_token = auth.create_access_token(user)
    assert len(access_token) > 0
