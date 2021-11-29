import requests
from pprint import pprint


class Loader:
    """ Class to get JSON data from requested URL address """

    API_TOKEN = "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"  # read until 02.10.2021
    DEFAULT_OWNER = "tishyk"
    DEFAULT_REPO = "Pyro5"
    DEFAULT_PARAMS = {"state": "open", }
    DEFAULT_HEADERS = {'Authorization': f'token {API_TOKEN}'}
    DEFAULT_QUERY_URL = f"https://api.github.com/repos/{DEFAULT_OWNER}/{DEFAULT_REPO}"

    def __init__(self, query_url, owner, repo):
        self.query_url = query_url
        self.owner = owner
        self.repo = repo
        self.call_count = 0

    @property
    def qurl(self):
        return f"{self.query_url}/{self.owner}/{self.repo}"

    # HW Create property setter and delleter for qurl attribute

    def get_json(self, params={}, headers={}, echo=False):
        request = requests.get(self.qurl,
                               headers=self.DEFAULT_HEADERS if not headers else headers,
                               params=self.DEFAULT_PARAMS if not params else params)
        assert request.ok, f"Failed to get requested page!"
        json_data = request.json()
        if echo:
            pprint(json_data)
        return json_data

    def __getattribute__(self, attribute_name):  # getattr(self, 'attribute_name')
        print(super().__getattribute__('call_count'))
        self.call_count = super().__getattribute__('call_count') + 1
        return super().__getattribute__(attribute_name)

    def __getattr__(self, attribute_name):
        print(f"There is no {attribute_name} in loader object")

    def __setattr__(self, key, value):
        print(f"Set item {key} with value {value}")
        super().__setattr__(key, value)


if __name__ == "__main__":
    loader = Loader("https://api.github.com/repos", "tishyk", "Pyro5")
    loader.get_json()
    print(loader.qurl)
    loader.repo = "flask-dropzone"
    print(loader.qurl)
    loader.get_json(echo=True)
    # loader.qurl = f"{loader.query_url}/{loader.owner}/{loader.repo}"
    print(loader.qurl)

    loader.attribute

