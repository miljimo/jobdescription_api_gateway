import os;

class Environment(object):

    @staticmethod
    def get(key, defaultVal=None):
        if type (key) != str:
            raise TypeError("key must be a string type but {0} given".format(type(key)))
        result = os.environ.get(key)
        if result is None:
            return defaultVal
        return result