from django.core.cache import caches


class Cache:
    
    RamCache = caches["default"]

    def get_cache(key: str, query: callable = lambda: any, timeout: int = 10, cache: any = RamCache) -> any:
        data = cache.get(key)
        if data is None:
            data = query()
            cache.set(key, data, timeout)
        return data


