from github_grabber import Loader

REPOSITORIES = ("Pyro5", "flask-dropzone")

class Repo:
    REPO_URL = "https://api.github.com/repos"
    REPO_USER = "tishyk"
    DEFAULT_REPO = "python_basics"

    def __init__(self, autoload=True, *args, **kwargs):
        self.repo = kwargs.get('repo', self.DEFAULT_REPO)
        if autoload:
            repo_loader = Loader(self.REPO_URL, self.REPO_USER, self.repo)
            self.load_attrs(repo_loader.get_json())

    def load_attrs(self, some_dict):
        """Method doc"""
        assert isinstance(some_dict, dict)
        self.__dict__.update(some_dict)
        print(f'Repo {self.name} object attributes updated')

    def __eq__(self, other):
        assert isinstance(other, self.__class__), "Not a Repo object"
        return self.repo == other.repo

    def __int__(self):
        return len(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        return self.repo

    def __dir__(self):
        return self.__dict__.keys()

    def __enter__(self):
        print("Context manager", self.repo, self.open_issues)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        repo = self.__dict__.get('repo', self.DEFAULT_REPO)
        self.__dict__.clear()
        self.repo = repo

    def __add__(self, other):
        new_object = self.__class__(repo=(self.repo, other.repo), autoload=False)
        for key, value in self.__dict__.items():
            new_object.__dict__[key] = (value, other.__dict__.get(key))
        return new_object

    def __sub__(self, other):
        assert isinstance(other, self.__class__), "Only Repo objects subtraction allowed!"
        new_repo = self.__class__(repo=self.repo, autoload=False)
        mismatch_count = 0
        for repo_key in self.__dict__:
            other_value = other.__dict__.get(repo_key, None)
            if other_value != self.__dict__[repo_key]:
                new_repo.__dict__[repo_key] = other_value
                mismatch_count += 1
        print(f"New object mismatch count {mismatch_count} out of {len(self.__dict__)}")
        return new_repo

    def __getitem__(self, item):
        assert item in self.__dict__, f"No '{item}' item found in repo '{self.repo}'"
        item_attribute = self.__dict__[item]

        if isinstance(item_attribute, dict):

            item_attribute = self.__class__(repo=f"{self.repo}_{item}", autoload=False)
            item_attribute.__dict__.update(self.__dict__[item])

        return item_attribute


if __name__ == "__main__":
    repo_pyro, repo_fd = (Repo(repo=repo) for repo in REPOSITORIES)
    rp = Repo(repo='Pyro5')
    print(repo_pyro == rp)  # --> True
    int(repo_pyro)  # --> len(self.__dict__)
    print(len(repo_pyro))

    with Repo('python_basics') as repo:
        print(repo, repo.open_issues_count)
        len(repo)

    nr_add = repo_pyro + repo_fd
    print(any(nr_add.open_issues_count))


    # nr_add.node_id # --> (repo_pyro.node_id, repo_fd.node_id)
    #
    nr_sub = repo_pyro - repo_fd

    repo_pyro['license']
    repo_parent = repo_pyro['parent']['owner']
    print(repo_parent.login)











