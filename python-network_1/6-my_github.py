#!/usr/bin/python3
"""
Fetches the GitHub user ID using the GitHub API with basic authentication.
"""

import requests
import sys

def fetch_github_id(username, password):
    """
    Fetches the GitHub user ID using the GitHub API.

    Args:
        username (str): The GitHub username.
        password (str): The personal access token.

    Returns:
        int: The GitHub user ID if the request is successful, otherwise None.
    """
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        return response.json()['id']
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./6-my_github.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    github_id = fetch_github_id(username, password)
    print(github_id if github_id is not None else "None")
