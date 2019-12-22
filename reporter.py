

import json
from influxdb import InfluxDBClient


class Reporter:

    influx_client = None  # connection to InfluxDB
    database = None  # name of database
    template = None  # template for object records

    def __init__(self, influx_host, influx_port, database_name='influx', location='olohuone', measurement='tflite_demo'):
        self.influx_client = self.connect_influx(influx_host, influx_port)
        self.database = database_name
        self.template = self.record_template(measurement, location)

    def connect_influx(self, host, port):
        return InfluxDBClient(host=host, port=port)

    def write_influx(self, list_of_data_dict):
        self.influx_client.switch_database(self.database)
        self.influx_client.write_points(list_of_data_dict)
    
    def disconnect_influx(self):
        self.influx_client.close()

    def record_template(self, measurement, location):
        """Creates a template for records.
        """
        tags = {
            'location': location,
            'object': None
        }

        fields = {
            'n_objects': None
        }

        return  {
                'measurement': measurement,
                'tags': tags,
                'fields': fields
        }

    def make_record(self, object, n_objects):
        """Creates a full record for writing.
        """
        import copy
        record = copy.deepcopy(self.template)
        # Note: self.template.copy() is not what we want
        record['tags']['object'] = object
        record['fields']['n_objects'] = n_objects
        #import datetime
        #record['time'] = datetime.datetime.now().isoformat()
        return record

    def to_influxjson(self, measurement, tags, fields):
        """
        influx_json = {
            "measurement": "alarms",
            "tags": {
                "deviceid": alarm_mqtt_json['id'],
                "type": alarm_mqtt_json['type'],
                "message": alarm_mqtt_json['message']
            },
            "fields": {
                "ntrigger": float(alarm_mqtt_json["ntrigger"])
            }
        }
        """

        influx_dict = {
            'measurement': measurement,
            'tags': tags,
            'fields': fields
        }

        return json.dumps(influx_dict)
