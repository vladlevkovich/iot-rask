from app.secruity.secruity import hash_password, check_password


def test_hash_password():
    password = 'password123'
    hashed = hash_password(password)
    assert hashed != password
    assert len(hashed) > 0


def test_check_password():
    password = 'password123'
    hashed = hash_password(password)
    assert check_password(hashed, password) is True
    assert check_password(hashed, 'fail_password') is False
