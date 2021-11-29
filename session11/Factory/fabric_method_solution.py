import json
import requests

from fabric_method_problem import Github_Pyro5, Github_Redfish

"""
How to Implement

1. Make all products follow the same interface. This interface should declare methods that make sense in every product.

2. Add an empty factory method inside the creator class.
    The return type of the method should match the common product interface.

3. In the creator’s code find all references to product constructors.
    One by one, replace them with calls to the factory method, while extracting the product creation code into the factory method.

4. Now, create a set of creator subclasses for each type of product listed in the factory method.
    Override the factory method in the subclasses and extract the appropriate bits of construction code from the base method.

5. If there are too many product types and it doesn’t make sense to create subclasses for all of them,
    you can reuse the control parameter from the base class in subclasses.

6. If, after all of the extractions, the base factory method has become empty, you can make it abstract.
    If there’s something left, you can make it a default behavior of the method.
"""


class GithubApi:
    # Update old code with factory method
    API_TOKEN = "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"
    USER = "tishyk"
    REPO = "Pyro5"

    def __init__(self):
        self.query_url = f"https://api.github.com/repos/{self.USER}/{self.REPO}"

    def get(self):
        params = {"state": "open", }
        headers = {'Authorization': f'token {self.API_TOKEN}'}
        return requests.get(self.query_url, headers=headers, params=params)

    @property
    def ok(self):
        return self.get().ok

    def json(self):
        return self.get().json()

    @classmethod
    def create_repo(cls, name, *args, **kwargs):
        if name == Github_Pyro5.REPO:
            repo = Github_Pyro5(*args, **kwargs)
        elif name == Github_Redfish.REPO:
            repo = Github_Redfish(*args, **kwargs)
        return repo


if __name__ == "__main__":
    # Some new test or code usage updated usage
    repo_pyro5 = GithubApi.create_repo('Pyro5')
    repo_redfish = GithubApi.create_repo('iDRAC-Redfish-Scripting')
    repo_redfish_save = GithubApi.create_repo('iDRAC-Redfish-Scripting', save=True)

    assert repo_pyro5.ok, f'Failed to get github repo "{repo_pyro5.repo}" data'

    if repo_pyro5.ok:
        with open('respond.json') as respond_file:
            assert repo_pyro5.json().get('name', '') == json.load(respond_file)['name'], "Owner Data mismatch!"

    if repo_redfish.ok:
        print("New repo object created")

    if repo_redfish_save.ok:
        repo_redfish_save.save_yaml()
