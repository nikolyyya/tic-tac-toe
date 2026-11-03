from sqlalchemy import select
from datasource.model.user import User as DatasourceUser
from datasource.mapper.user_mapper import datasource_to_domain, domain_to_datasource
from domain.exception.user_already_exists import UserAlreadyExists
from sqlalchemy.exc import IntegrityError

class UserRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def save(self, domain_user):
        datasource_user = domain_to_datasource(domain_user)
        with self.session_factory() as db:
            db.add(datasource_user)
            try:
                db.commit()
            except IntegrityError:
                raise UserAlreadyExists()
            return datasource_to_domain(datasource_user)
            
            

    def get_by_login(self, login):
        with self.session_factory() as db:
            result = db.scalars(select(DatasourceUser).where(DatasourceUser.login == login)).one_or_none()

            if result is None:
                return None

            return datasource_to_domain(result)
            


    def get_by_id(self, user_id):
        with self.session_factory() as db:
            user = db.get(DatasourceUser, user_id)
            if user:
                return datasource_to_domain(user)
            return None
