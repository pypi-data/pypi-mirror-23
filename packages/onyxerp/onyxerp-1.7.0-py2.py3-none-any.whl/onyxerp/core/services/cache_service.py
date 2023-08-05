import json


class CacheService(object):

    @staticmethod
    def read_file(file_name):
        handle = open(file_name, "r")
        json_data = json.loads(handle.read())
        handle.close()
        return json_data

    @staticmethod
    def write_file(file_name, data):
        handle = open(file_name, "w+")
        handle.write(json.dumps(data))
        handle.close()
        return True
