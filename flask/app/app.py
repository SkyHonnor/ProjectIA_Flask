from flask import Flask
from database import init_database
from influxdb import init_influxdatabase
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

init_database(app)
init_influxdatabase(app)

from routes import route_temperature
app.register_blueprint(route_temperature.temperature_page, url_prefix="/temperature")

from routes import route_scikit
app.register_blueprint(route_scikit.scikit_page, url_prefix="/scikit")

from routes import route_chinook 
app.register_blueprint(route_chinook.chinook_page, url_prefix="/chinook")

from routes import route_influxdb
app.register_blueprint(route_influxdb.influxdb_page, url_prefix="/influxdb")

from routes import route_classifieur
app.register_blueprint(route_classifieur.classifieur_page, url_prefix="/classifieur")

from routes import route_main
app.register_blueprint(route_main.main_page)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80, debug=True)