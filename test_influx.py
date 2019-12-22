
from influxdb import InfluxDBClient
import json
import time
from reporter import Reporter

influx_host = "157.230.98.123"
influx_port = 8087
influx_db = 'influx'


tags = {
    'location': 'olohuone',
    'object': 'person'
}

fields = {
    'n_objects': 4
}

#data_json_str = reporter.to_influxjson('tflite_demo', tags, fields)
data_dict = {
        'measurement': 'tflite_demo',
        'tags': tags,
        'fields': fields
    }

rp = Reporter(influx_host, influx_port)
rp.write_influx([rp.make_record('dog', 4), rp.make_record('cat', 6)])
time.sleep(2)
rp.write_influx([rp.make_record('person', 4)])
#time.sleep(5)
#data_dict['fields']['n_objects'] = 5
#rp.write_influx('influx', data_dict)

rp.disconnect_influx()


"""
db_client = reporter.connect_influx(influx_host, influx_port)
reporter.write_influx(db_client, 'influx', data_dict)
"""

"""
influx_client = InfluxDBClient(host=influx_host, port=influx_port)
influx_client.switch_database(influx_db)
influx_client.write_points([data_dict])
influx_client.close()
"""
