import os

class Config:
    INFLUXDB_V2_URL = "http://192.168.168.88:8086"
    INFLUXDB_V2_ORG = "IUT"
    INFLUXDB_V2_TOKEN = 'gQMgdAee398j6l9G6f5LcDNXwNJONYcPX5MDP-oZlX8oiVfkojD7nl-SnmA9BHI2drpgIAlWIjf-3e1WPejcqw=='

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database/chinook.db')
