from flask import Blueprint, render_template
from influxdb import client as influxclient
import pandas as pd
import matplotlib.pyplot as plt

influxdb_page = Blueprint("influxdb_page", __name__)

@influxdb_page.route('/bitcoin')
def bitcoin():
    query_api = influxclient.query_api()
    query = '''
        from(bucket: "Bitcoin") |> range(start: -10h) |> limit(n:99)
    '''
    
    result = query_api.query(query)

    timeserie = generate_dataframe(result)

    timeserie['time'] = pd.to_datetime(timeserie['time'])

    group_size =int(len(timeserie)/3)
    group1 = timeserie.iloc[:group_size-3]
    group2 = timeserie.iloc[group_size-3:2*group_size-6]
    group3 = timeserie.iloc[2*group_size-6:]

    plt.figure(figsize=(10, 6))
    plt.plot(group1['time'], group1['value'], marker='o', linestyle='-', color='b', label='€')
    plt.plot(group2['time'], group2['value'], marker='o', linestyle='-', color='r', label='$')
    plt.plot(group3['time'], group3['value'], marker='o', linestyle='-', color='g', label='£')
    plt.title('Évolution du cours du Bitcoin')
    plt.legend()
    plt.xlabel('Temps')
    plt.ylabel('Valeur')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/img/bitcoin_plot.png')

    return render_template('influxdb/bitcoin.html', table=timeserie.to_html(classes="table table-striped"))

@influxdb_page.route('/buckets')
def buckets():
    return render_template('influxdb/bitcoin.html')

    # buckets_api = influxclient.buckets_api()
    # buckets = buckets_api.find_buckets().buckets
    # bucket_list = [{"id": b.id, "name": b.name} for b in buckets]

def generate_dataframe(result):
    data = []
    for table in result:
        for record in table.records:
            data.append({
                "time": record.get_time(),
                "value": record.get_value()
            })
    return pd.DataFrame(data)

