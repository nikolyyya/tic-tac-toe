
import uuid

from datasource.database import SessionLocal
from datasource.repository.user_repository import UserRepository
from domain.model.user import User


repository = UserRepository(SessionLocal)


# 1. Проверяем сохранение пользователя
user = User.new("test_login", "12345")

saved_user = repository.save(user)

assert saved_user.login == "test_login"
assert saved_user.id == user.id

print("save() работает")


# 2. Проверяем поиск по логину
found_user = repository.get_by_login("test_login")

assert found_user is not None
assert found_user.login == "test_login"

print("get_by_login() работает")


# 3. Проверяем поиск по несуществующему логину
not_found = repository.get_by_login("unknown_login")

assert not_found is None

print("get_by_login() для несуществующего пользователя работает")


# 4. Проверяем поиск по ID
found_by_id = repository.get_by_id(user.id)

assert found_by_id is not None
assert found_by_id.id == user.id

print("get_by_id() работает")


# 5. Проверяем поиск по несуществующему ID
not_found_by_id = repository.get_by_id(uuid.uuid4())

assert not_found_by_id is None

print("get_by_id() для несуществующего пользователя работает")


print("\nВсе тесты пройдены!")
