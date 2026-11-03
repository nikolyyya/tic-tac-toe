import uuid
from werkzeug.security import generate_password_hash, check_password_hash


class User:
    def __init__(self, id: uuid.UUID, login, password_hash):
        self.id = id
        self.login = login
        self.password_hash = password_hash

    @staticmethod
    def new(login, password):
        new_id = uuid.uuid4()
        password_hash = generate_password_hash(password, salt_length=16)
        return User(new_id, login, password_hash)

    def check_hash(self, password):
        valid = check_password_hash(self.password_hash, password)
        return valid