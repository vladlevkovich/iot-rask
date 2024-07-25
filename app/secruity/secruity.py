import bcrypt


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def check_password(password_hash, plain_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), password_hash.encode('utf-8'))
