from github_grabber_from_1_session import GithubApi


# Abstract Factory is a creational design pattern that lets you
# produce families of related objects without specifying their concrete classes.

# Use the Abstract Factory when your code needs to work with various families of related products,
# but you don’t want it to depend on the concrete classes of those products—they might be unknown beforehand
# or you simply want to allow for future extensibility.

# We have different repo names already, but what if we need to test/run them
# with different API_Tokens or different user names

# Will it be something like this?

class Github_Pyro5_USER1(GithubApi):
    REPO = "Pyro5"
    USER = "tishyk"


class Github_Redfish_USER1(GithubApi):
    REPO = "iDRAC-Redfish-Scripting"
    USER = "tishyk"


class Github_Pyro5_USER_2(GithubApi):
    REPO = "Pyro5"
    USER = "dell"


class Github_Redfish_USER2(GithubApi):
    REPO = "iDRAC-Redfish-Scripting"
    USER = 'dell'


# Next possible changes will create more class variants

class Github_Pyro5_USER1_Token2(GithubApi):
    REPO = "Pyro5"
    USER = "tishyk"
    API_TOKEN = "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"


class Github_Redfish_USER1_Token2(GithubApi):
    REPO = "iDRAC-Redfish-Scripting"
    USER = "tishyk"
    API_TOKEN = "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"


class Github_Pyro5_USER_2_Token2(GithubApi):
    REPO = "Pyro5"
    USER = "dell"
    API_TOKEN = "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"


class Github_Redfish_USER2_Token2(GithubApi):
    REPO = "iDRAC-Redfish-Scripting"
    USER = 'dell'
    API_TOKEN = "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"

# And more and more changes ... But in different files usually ...
