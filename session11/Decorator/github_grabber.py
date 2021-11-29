import requests
from functools import lru_cache, singledispatch, update_wrapper


def mysingledispatch(func):
    dispatcher = singledispatch(func)

    def wrapper(*args, **kw):
        if len(args) == 1:
            return dispatcher.dispatch(args[0].__class__)(*args, **kw)
        else:
            return dispatcher.dispatch(args[1].__class__)(*args, **kw)

    wrapper.register = dispatcher.register
    update_wrapper(wrapper, func)
    return wrapper


class ProxyRequest:
    URLS_CACHE = {}

    def __init__(self, url, params, headers):
        self.params = params
        self.headers = headers
        self.url = url
        self.__respond = requests.get(url, params=params, headers=headers)
        self.__class__.URLS_CACHE.setdefault(self.url, self.__respond)

    @property
    def respond(self):
        return self.URLS_CACHE.get(self.url, self.__respond)


class GithubApi():
    API_TOKEN = "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"
    API_TOKEN1 = "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"

    USER = "tishyk"
    REPO = "Pyro5"

    def __init__(self):
        self.query_url = f"https://api.github.com/repos/{self.USER}/{self.REPO}"

    @mysingledispatch
    def get(self, token=None):
        # Python 3.8, functools.singledispatchmethod allows single dispatch on methods, classmethods, abstractmethods, and staticmethods.
        params = {"state": "open", }
        headers = {'Authorization': f'token {self.API_TOKEN}'}
        return requests.get(self.query_url, headers=headers, params=params)

    @get.register(list)
    def _(self, token):
        respond = []
        params = {"state": "open", }
        for _token in token:
            headers = {'Authorization': f'token {_token}'}
            respond.append(requests.get(self.query_url, headers=headers, params=params))
        return respond # []

    @property  # cached_property for python 3.9
    def ok(self):
        return self.get().ok

    @lru_cache(maxsize=None, typed=True)
    def get_json(self,):
        return self.get().json()
