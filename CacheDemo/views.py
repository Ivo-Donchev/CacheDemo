from django.contrib.auth.models import User
from django.views import View
from django.http.response import HttpResponse
from django.core.cache import caches

dummy_cache = {}


class IndexView(View):
    def get(self, request):
        # Some hard calculations
        ########################
        import time
        time.sleep(2)
        ########################

        return HttpResponse(User.objects.values_list())


class DummyDummyCachedView(IndexView):
    cache_key = 'dummy_cache_key'

    def get(self, request):
        cached_response = dummy_cache.get(self.cache_key)

        if cached_response:
            return cached_response

        response = super().get(request)
        dummy_cache[self.cache_key] = response

        return response


class LocMemCachedView(IndexView):
    cache_key = 'locmemcache_key'

    def get(self, request):
        cache = caches['locmem']
        cached_response = cache.get(self.cache_key)

        if cached_response:
            return cached_response

        response = super().get(request)
        cache.set(self.cache_key, response)

        return response


class MemcachedView(IndexView):
    cache_key = 'memcache_key'

    def get(self, request):
        cache = caches['memcache']
        cached_response = cache.get(self.cache_key)

        if cached_response:
            return cached_response

        response = super().get(request)
        cache.set(self.cache_key, response)

        return response


class DBCachedView(IndexView):
    cache_key = 'db_cache_key'

    def get(self, request):
        cache = caches['db']
        cached_response = cache.get(self.cache_key)

        if cached_response:
            return cached_response

        response = super().get(request)
        cache.set(self.cache_key, response)

        return response


class FileSystemCachedView(IndexView):
    cache_key = 'filesystem_cache_key'

    def get(self, request):
        cache = caches['filesystem']
        cached_response = cache.get(self.cache_key)

        if cached_response:
            return cached_response

        response = super().get(request)
        cache.set(self.cache_key, response)

        return response


class RedisView(IndexView):
    cache_key = 'django_redis_key'

    def get(self, request):
        cache = caches['redis']
        cached_response = cache.get(self.cache_key)

        if cached_response:
            return cached_response

        response = super().get(request)
        cache.set(self.cache_key, response)

        return response


class RedisCacheView(IndexView):
    cache_key = 'django_redis_cache_key'

    def get(self, request):
        cache = caches['redis_cache']
        cached_response = cache.get(self.cache_key)

        if cached_response:
            return cached_response

        response = super().get(request)
        cache.set(self.cache_key, response)

        return response


class RaceCondLocMemCachedView(IndexView):
    cache_key = 'locmem_counter'

    def get(self, request):
        cache = caches['locmem']
        cached_response = cache.get(self.cache_key)

        if cached_response:
            cache.set(self.cache_key, cached_response + 1)
            return HttpResponse(cached_response)

        cache.set(self.cache_key, 1)
        return HttpResponse(1)
