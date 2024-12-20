import requests

token = "your_github_token"
headers = {"Authorization": f"token {token}"}
url = "https://api.github.com/user/repos"

total_size = 0
while url:
    response = requests.get(url, headers=headers).json()
    for repo in response:
        total_size += repo['size']  # Size is in KB
    # Check for pagination
    url = response.links['next']['url'] if 'next' in response.links else None

print(f"Total storage used: {total_size / 1024:.2f} MB")
