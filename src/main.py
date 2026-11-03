from web.module.flask_app import app
from datasource.database import Base, engine
from datasource.model.game import Game as DatasourceGame # noqa: F401
from datasource.model.user import User # noqa: F401
import web.route.game_route # noqa: F401


if __name__ == ("__main__"):
    Base.metadata.create_all(bind=engine)
    app.run(debug=True)