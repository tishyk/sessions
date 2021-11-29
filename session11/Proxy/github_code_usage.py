import json
from github_grabber_with_proxy_request import GithubApi
# from fabric_method_solution import GithubApi

# Let's assume this is some old code or test.
# This code should always work after GithubApi class refactoring

if __name__ == "__main__":
    # Some test or code usage
    github = GithubApi()
    assert github.ok, f'Failed to get github repo "{github.REPO}" data'
    content = github.get().content
    json_cont = github.json()
    if github.ok:
        with open('respond.json') as respond_file:
            # json.dump(github.json(), respond_file, indent=3)
            assert github.json() == json.load(respond_file), "Data mismatch!"

    if github.ok:
        with open('respond.json') as respond_file:
            assert github.json().get('owner', '') == json.load(respond_file)['owner'], "Owner Data mismatch!"

