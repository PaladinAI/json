# JSON

Catch2 is a C++ JSON library used by the [Collector](https://github.com/PaladinAI/ddat-collector),
[Local Agent](https://github.com/PaladinAI/ddat-localagent) and
[Platform](https://github.com/PaladinAI/ddat-platform).

# Syncing with the upstream master branch

First, make sure the `upstream` remote is configured:

    git remote -v

    # If the upstream remote doesn't exist, add it:
    git remote add upstream https://github.com/nlohmann/json.git

Then merge the upstream changes

    git fetch upstream
    git checkout develop
    git merge upstream/develop

# Publishing to the Conan server

To update the package, update the version number in `conanfile.py` then run:

    conan create . paladin/develop
    conan upload json/3.2.0@paladin/develop -r paladin
