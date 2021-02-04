import simplejson


def read_json_file(file_path: str) -> dict:
    data = {}
    with open(file_path) as json_file:
        data = simplejson.load(json_file)
    return data
