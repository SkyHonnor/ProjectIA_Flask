from influxdb_client import InfluxDBClient, Point, WritePrecision

def init_influxdatabase(app):
    global client
    client = InfluxDBClient(
        url=app.config['INFLUXDB_V2_URL'],
        token=app.config['INFLUXDB_V2_TOKEN'],
        org=app.config['INFLUXDB_V2_ORG']
    )
