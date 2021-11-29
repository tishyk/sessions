import requests
from abc import ABC, abstractmethod


# API_TOKEN = "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"  # until 02.10.2021
# owner = "tishyk"
# repo = "Pyro5"
# query_url = f"https://api.github.com/repos/{'dell'}/{'iDRAC-Redfish-Scripting'}"
# params = {"state": "open", }
# headers = {'Authorization': f'token {API_TOKEN}'}
#
# r = requests.get(query_url, headers=headers, params=params)
#
# json_data = r.json()

# if __name__ == "__main__":
#     pprint(json_data)

# Github user created with all admin credentials.


class ProxyRequest:
    URLS_CACHE = {}

    def __init__(self, url, params, headers):
        self.params = params
        self.headers = headers
        self.url = url
        if not self.__class__.URLS_CACHE.get(self.url, {}):
            self.__respond = requests.get(url, params=params, headers=headers)
            self.__class__.URLS_CACHE.setdefault(self.url, self.__respond)
        else:
            self.__respond =  self.__class__.URLS_CACHE.get(self.url)

    @property
    def respond(self):
        return self.URLS_CACHE.get(self.url, self.__respond)


class GithubApi():
    API_TOKEN = "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" # no expiration, read only
    USER = "tishyk"
    REPO = "Pyro5"

    def __init__(self):
        self.query_url = f"https://api.github.com/repos/{self.USER}/{self.REPO}"

    def get(self):
        params = {"state": "open", }
        headers = {'Authorization': f'token {self.API_TOKEN}'}
        #respond = requests.get(self.query_url, headers=headers, params=params)
        # ProxyRequest(self.query_url, headers=headers, params=params)
        resp = ProxyRequest(self.query_url, headers=headers, params=params).respond
        print(id(resp))
        return resp

    @property
    def ok(self):
        return self.get().ok

    def json(self):
        return self.get().json()





