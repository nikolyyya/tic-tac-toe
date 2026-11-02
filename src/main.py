from web.module.flask_app import app
from datasource.database import Base, engine
from datasource.model.game import Game as DatasourceGame
import web.route.game_route


if __name__ == ("__main__"):
    Base.metadata.create_all(bind=engine)
    app.run(debug=True)