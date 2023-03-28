import requests
import json

GITHUB_BASE_URL = "https://api.github.com"

def create_repo(token, module, owner, is_org = True):
    url = "%(base_url)s/%(user_uri)s/repos" % {
        'base_url': GITHUB_BASE_URL,
        'user_uri': f'org/{owner}' if is_org else 'user',
    }

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer %s' % token,
        'X-GitHub-Api-Version': '2022-11-28'
    }

    body = {
        'name': module,
        'gitignore_template': 'Python',
        'private': True
    }

    response = requests.post(url, headers=headers, data=json.dumps(body))

    status_code = response.status_code
    if status_code != 200:
        raise Exception(f"Status code: {status_code}. Url: {url}. Context: {response.text}")