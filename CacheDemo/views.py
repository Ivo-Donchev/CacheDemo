from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse
from django.core.cache import cache


class IndexView(View):
    def get(self, request):
        import time
        time.sleep(3)
        return HttpResponse("good")


class CachedView(IndexView):
    def get(self, request):
        cached_response = cache.get('my_cache_key')

        if cached_response:
            return cached_response

        response = super().get(request)
        cache.set('my_cache_key', response)

        return response
