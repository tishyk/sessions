import requests
from abc import ABC, abstractmethod
from github_grabber_from_1_session import GithubApi

# Abstract Factory is a creational design pattern that lets you
# produce families of related objects without specifying their concrete classes.

"""
How to Implement

1. Map out a matrix of distinct product types versus variants of these products (repo_absfact_variants.png)

2. Declare abstract product interfaces for all product types. Then make all concrete product classes implement these interfaces.

3. Declare the abstract factory interface with a set of creation methods for all abstract products.

4. Implement a set of concrete factory classes, one for each product variant.

5. Create factory initialization code somewhere in the app.
    It should instantiate one of the concrete factory classes, depending on the application configuration or the current environment. 
    Pass this factory object to all classes that construct products.

6. Scan through the code and find all direct calls to product constructors. 
    Replace them with calls to the appropriate creation method on the factory object.
"""


# 2

class AbstractGithubApiRepo(ABC):
    # Abstract repo/product
    @abstractmethod
    def __init__(self):
        self.query_url = f"https://api.github.com/repos/{self.USER}/{self.REPO}"

    @abstractmethod
    def get(self):
        params = {"state": "open", }
        headers = {'Authorization': f'token {self.API_TOKEN}'}
        return requests.get(self.query_url, headers=headers, params=params)

    @property
    @abstractmethod
    def ok(self):
        return self.get().ok

    @abstractmethod
    def json(self):
        return self.get().json()


class Repo5(AbstractGithubApiRepo):
    def __init__(self):
        super().__init__()

    def get(self):
        return super().get()

    @property
    def ok(self):
        return super().ok

    def json(self):
        return super().json()


class Redfish(Repo5, AbstractGithubApiRepo):
    def __init__(self, user='tishyk', repo='"iDRAC-Redfish-Scripting"', save=False):
        self.USER = user
        self.REPO = repo
        self.save = save
        super().__init__()


class OtherRepo(Repo5):
    pass


class AbstractGithubApiFactory(ABC):
    # Abstract Factory. Access point to all possible combinations of the repos, users, tokens etc.
    @classmethod
    @abstractmethod
    def create_Repo5(cls):
        pass

    @classmethod
    @abstractmethod
    def create_Redfish(cls):
        pass

    @classmethod
    @abstractmethod
    def create_other_repo(cls):
        pass


class DefaultApiFactory(AbstractGithubApiFactory):

    @classmethod
    def create_Repo5(self):
        Repo5.USER = "tishyk"
        Repo5.REPO = "Pyro5"
        repo5 = Repo5()  # In case of old code support needed
        repo5.USER = "tishyk"  # Shadow class variables from previous examples
        repo5.REPO = "Pyro5"  # Shadow class variables from previous examples
        repo5.API_TOKEN = TokenApiFactory.DEFAULT_TOKEN
        repo5.__init__()  # update initial values
        return repo5

    @classmethod
    def create_Redfish(self, save=False):
        redfish = Redfish(user=UserApiFactory.DEFAULT_USER, save=save)
        redfish.API_TOKEN = TokenApiFactory.DEFAULT_TOKEN
        return redfish

    @classmethod
    def create_other_repo(self):
        # The same action for any other repo name
        pass


class UserApiFactory(AbstractGithubApiFactory):
    DEFAULT_USER = 'tishyk'
    USER = 'dell'

    @classmethod
    def create_Repo5(self):
        Repo5.USER = UserApiFactory.USER
        Repo5.REPO = "Pyro5"
        repo5 = Repo5()  # In case of old code support needed
        repo5.USER = UserApiFactory.USER  # Shadow class variables from previous examples
        repo5.REPO = "Pyro5"  # Shadow class variables from previous examples
        repo5.__init__()  # update initial values
        return repo5

    @classmethod
    def create_Redfish(self):
        redfish = Redfish(user=UserApiFactory.USER)
        redfish.API_TOKEN = TokenApiFactory.DEFAULT_TOKEN
        return redfish

    @classmethod
    def create_other_repo(self):
        pass


class TokenApiFactory(AbstractGithubApiFactory):
    DEFAULT_TOKEN = "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"
    USER_TOKEN = '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'

    @classmethod
    def create_Repo5(self):
        Repo5.USER = UserApiFactory.DEFAULT_USER
        Repo5.REPO = "Pyro5"
        repo5 = Repo5()  # In case of old code support needed
        repo5.USER = UserApiFactory.DEFAULT_USER  # Shadow class variables from previous examples
        repo5.REPO = "Pyro5"  # Shadow class variables from previous examples
        repo5.__init__()  # update initial values
        return repo5

    @classmethod
    def create_Redfish(self):
        redfish = Redfish()
        redfish.API_TOKEN = self.USER_TOKEN

    @classmethod
    def create_other_repo(self):
        pass


if __name__ == "__main__":
    repo5_default = DefaultApiFactory.create_Repo5()
    repo5_2nd_user = UserApiFactory.create_Repo5()
    repo5_2nd_token = TokenApiFactory.create_Repo5()

    redfish_default = DefaultApiFactory.create_Redfish()
    redfish_2nd_user = UserApiFactory.create_Redfish()
    redfish_2nd_token = TokenApiFactory.create_Redfish()


