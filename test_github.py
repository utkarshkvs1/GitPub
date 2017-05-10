import pytest
import github


def test_load_gh_profile():
    """
    Tests github.Profile.load_gh_profile() by loading details of the user `demfier`
    ------------------------------------------------------------------------------
    Parameters: None
    """

    test_username = 'demfier'
    # define the validation Profile
    correct = github.Profile(username="demfier", name="Gaurav",
                             location="Kharagpur, West Bengal",
                             email="sahu.gaurav719@gmail.com", followers_count=10,
                             repos_url="https://api.github.com/users/Demfier/repos",
                             public_repo_count=14)

    profile = github.Profile()
    # load github profile of the user
    profile.load_gh_profile('demfier')

    # validations
    assert profile.username == correct.username
    assert profile.name == correct.name
    assert profile.email == correct.email
    assert profile.followers_count == correct.followers_count
    assert profile.repos_url == correct.repos_url
    assert profile.location == correct.location
    assert profile.public_repo_count == correct.public_repo_count


def test_get_public_repos():
    """
    Tests github.Profile.get_public_repos() by loading public repository details
    of the user `demfier`
    ----------------------------------------------------------------------------
    Parameters: None
    """

    test_username = 'demfier'
    # define the validation Profile
    correct = github.Profile(username="demfier", name="Gaurav",
                             location="Kharagpur, West Bengal",
                             email="sahu.gaurav719@gmail.com", followers_count=10,
                             repos_url="https://api.github.com/users/Demfier/repos",
                             public_repo_count=14)

    # get public repos for the validation Profile
    correct.get_public_repos()

    profile = github.Profile()
    profile.load_gh_profile('demfier')
    profile.get_public_repos()

    # validations
    for idx, _ in enumerate(profile.public_repos):
        assert profile.public_repos[idx].name == correct.public_repos[idx].name
