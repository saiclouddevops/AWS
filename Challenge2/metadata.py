import requests
import json
from sys import argv

metadata_url = 'http://169.254.169.254/latest/'



def reuse(url, arr):
    output = {}
    for item in arr:
        new_url = url + item
        r = requests.get(new_url)
        text = r.text
        if item[-1] == "/":
            list_of_values = r.text.splitlines()
            output[item[:-1]] = reuse(new_url, list_of_values)
        elif is_json(text):
            output[item] = json.loads(text)
        else:
            output[item] = text
    return output


def get_metadata():
    initial = ["meta-data/"]
    result = reuse(metadata_url, initial)
    return result


def get_metadata_json():
    metadata = get_metadata()
    metadata_json = json.dumps(metadata, indent=4, sort_keys=True)
    return metadata_json


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


def search_value(json_object,key):
    return json_object["meta-data"][key]

if __name__ == '__main__':
    json_object=get_metadata_json()
    print(json_object)
    json_object=json.loads(json_object)
    print("=====search by key=====")
    print(search_value(json_object,argv[1]))
