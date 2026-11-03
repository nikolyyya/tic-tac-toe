from domain.model.user import User as DomainUser
from datasource.model.user import User as DatasourceUser

def domain_to_datasource(domain_user):
    datasource_user = DatasourceUser(id=domain_user.id, login=domain_user.login, password_hash=domain_user.password_hash)
    return datasource_user

def datasource_to_domain(datasource_user):
    domain_user = DomainUser(datasource_user.id, datasource_user.login, datasource_user.password_hash)
    return domain_user