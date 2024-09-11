import os
import requests
from dotenv import load_dotenv
import pytest

load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")

def test_github_api():

    create_repo_url = f"https://api.github.com/user/repos"
    create_repo_data = {"name": REPO_NAME, "private": False}
    response = requests.post(create_repo_url, json=create_repo_data, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    assert response.status_code == 201


    repos_url = f"https://api.github.com/user/repos"
    response = requests.get(repos_url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    assert response.status_code == 200
    assert any(repo["name"] == REPO_NAME for repo in response.json())


    delete_repo_url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}"
    response = requests.delete(delete_repo_url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    assert response.status_code == 204