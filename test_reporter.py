
import json
import reporter


tags = {
    'location': 'olohuone',
    'object': 'person'
}

fields = {
    'n_objects': 4
}

data_json_str = reporter.to_influxjson('tflite_demo', tags, fields)

data_json = json.loads(data_json_str)
print(json.dumps(data_json, indent=4))
