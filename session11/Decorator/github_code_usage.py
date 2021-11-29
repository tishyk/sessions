import json
import time
from github_grabber import GithubApi
import timeout_decorator

@timeout_decorator.timeout(5)
def run():
    print("Start")
    for i in range(1,10):
        time.sleep(1)
        print("{} seconds have passed".format(i))

if __name__ == "__main__":
    # Some test or code usage
    github = GithubApi()
    assert github.ok, f'Failed to get github repo "{github.repo}" data'
    #
    # if github.ok:
    #     with open('respond.json') as respond_file:
    #         x = github.get_json()

    # print(github.get_json.cache_info())
    # github.get_json.cache_clear()
    # print(github.get_json.cache_info())

    github.get([github.API_TOKEN, github.API_TOKEN1])

    run()
