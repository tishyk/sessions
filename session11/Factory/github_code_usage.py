import json
from github_grabber_from_1_session import GithubApi
# from fabric_method_solution import GithubApi

# Let's assume this is some old code or test.
# This code should always work after GithubApi class refactoring

if __name__ == "__main__":
    # Some test or code usage
    github = GithubApi()
    assert github.ok, f'Failed to get github repo "{github.repo}" data'

    if github.ok:
        with open('respond.json') as respond_file:
            assert github.json() == json.load(respond_file), "Data mismatch!"

    if github.ok:
        with open('respond.json') as respond_file:
            assert github.json().get('owner', '') == json.load(respond_file)['owner'], "Owner Data mismatch!"

