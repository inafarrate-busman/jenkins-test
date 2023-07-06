import requests
import json
import re

GITHUB_BASE_URL = "https://api.github.com"

def create_repo(token, module, owner, is_org = True):
    url = "%(base_url)s/%(user_uri)s/repos" % {
        'base_url': GITHUB_BASE_URL,
        'user_uri': f'orgs/{owner}' if is_org else 'user',
    }

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer %s' % token,
        'X-GitHub-Api-Version': '2022-11-28'
    }

    body = {
        'name': module.lower(),
        'gitignore_template': 'Python',
        'private': True
    }

    response = requests.post(url, headers=headers, data=json.dumps(body))

    status_code = response.status_code
    if status_code != 201:
        raise Exception(f"Status code: {status_code}. Url: {url}. Context: {response.text}")

def rename_main_branch(token, module, owner, new_branch, main_branch = 'main'):
    url = "%(base_url)s/repos/%(owner)s/%(module)s/branches/%(main_branch)s/rename" % {
        'base_url': GITHUB_BASE_URL,
        'owner': owner,
        'module': module,
        'main_branch': main_branch.lower()
    }

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer %s' % token,
        'X-GitHub-Api-Version': '2022-11-28'
    }

    body = {
        'new_name': new_branch.lower(),
    }

    response = requests.post(url, headers=headers, data=json.dumps(body))

    status_code = response.status_code

    if status_code != 201:
        raise Exception(f"Status code: {status_code}. Url: {url}. Context: {response.text}")

    result_data = response.json()

    commit = result_data.get('commit', {})
    branch_sha = commit.get('sha', False)

    return branch_sha

def create_new_branch(token, module, owner, new_branch, from_branch_sha):
    url = "%(base_url)s/repos/%(owner)s/%(module)s/git/refs" % {
        'base_url': GITHUB_BASE_URL,
        'owner': owner,
        'module': module.lower()
    }

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer %s' % token,
        'X-GitHub-Api-Version': '2022-11-28'
    }

    body = {
		"ref": "refs/heads/%(branch)s" % {"branch": new_branch},
        "sha": from_branch_sha
    }

    response = requests.post(url, headers=headers, data=json.dumps(body))
    status_code = response.status_code

    if status_code != 201:
        raise Exception(f"Status code: {status_code}. Url: {url}. Context: {response.text}")
    
def merge_dev_branch(token, module, owner, dev_branch, main_branch):
    url = "%(base_url)s/repos/%(owner)s/%(module)s/merges" % {
        'base_url': GITHUB_BASE_URL,
        'owner': owner,
        'module': module.lower()
    }

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer %s' % token,
        'X-GitHub-Api-Version': '2022-11-28'
    }

    body = {
        "base": main_branch.lower(),
        "head": dev_branch.lower(),
    }

    response = requests.post(url, headers=headers, data=json.dumps(body))

    status_code = response.status_code
    if status_code not in [201, 204]:
        raise Exception(f"Status code: {status_code}. Url: {url}. Context: {response.text}")
    
def get_dev_branch(main_branch):
    return f"{main_branch.lower()}_dev"

def check_brach_name(branch_name):
    regex = r"^\d{2}\.\d$"
    match = re.search(regex, branch_name)

    if not match:
        raise Exception(f"La rama {branch_name} no es válida.")