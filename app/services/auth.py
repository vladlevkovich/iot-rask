from datetime import datetime, timedelta
import jwt


class JWTAuth:
    """Генерація токена"""
    def __init__(self, secret: str = 'secret', algorithm: str = 'HS256'):
        self.secret = secret
        self.algorithm = algorithm

    def create_access_token(self, user: dict, expire: int = None):
        if not expire:
            expire = datetime.now() + timedelta(days=2)     # час життя токена
        paylaod = {
            'id': user['id'],
            'email': user['email'],
            'type': 'access',
            'exp': expire
        }
        access_token = jwt.encode(paylaod, self.secret, algorithm=self.algorithm)
        return access_token


auth = JWTAuth()
