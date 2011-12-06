from django.core.cache import cache
from hashlib import sha224
import pickle

def method_cache(seconds=0):
    def inner_cache(method):
        def x(instance, *args, **kwargs):
            key = sha224(str(method.__module__) + str(method.__name__) + \
                         str(id(instance)) + str(args) + str(kwargs)).hexdigest()
            result = cache.get(key)
            if result is None:
                result = method(instance, *args, **kwargs)
                if seconds and isinstance(seconds, int):
                    cache.set(key, pickle.dumps(result, -1), seconds)
            else:
                result = pickle.loads(result)
            return result
        return x
    return inner_cache
