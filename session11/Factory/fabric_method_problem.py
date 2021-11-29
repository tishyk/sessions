import json
import yaml
from github_grabber_from_1_session import GithubApi


# 1. Use the Factory Method when you don’t know beforehand the exact types
# and dependencies of the objects your code should work with.

# 2. Use the Factory Method when you want to provide users of your library
# or framework with a way to extend its internal components.

# 3. Use the Factory Method when you want to save system resources by reusing existing objects
# instead of rebuilding them each time.

# !!! The Factory Method separates product construction code from the code that actually uses the product. !!!

# Let's assume this is some new code or test.
# This code should always work with initial github repo name and should have additional repo names


class Github_Pyro5(GithubApi):
    REPO = "Pyro5"


class Github_Redfish(GithubApi):
    REPO = "iDRAC-Redfish-Scripting"

    def __init__(self, save=False):
        self.save = save
        super().__init__()

    def save_yaml(self):
        if self.ok and self.save:
            with open('respond.yaml', 'w') as f:
                yaml.dump(self.get().json(), f)
        else:
            print("Skip data save into yaml")


if __name__ == "__main__":
    # Some new test or code usage
    repo_pyro5 = Github_Pyro5()
    repo_redfish = Github_Redfish()
    repo_redfish_save = Github_Redfish(save=True)

    assert repo_pyro5.ok, f'Failed to get github repo "{repo_pyro5.repo}" data'

    if repo_pyro5.ok:
        with open('respond.json') as respond_file:
            assert repo_pyro5.json().get('name', '') == json.load(respond_file)['name'], "Owner Data mismatch!"

    if repo_redfish.ok:
        print("New repo object created")

    if repo_redfish_save.ok:
        repo_redfish_save.save_yaml()
