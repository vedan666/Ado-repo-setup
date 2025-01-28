import requests
import base64
import json

def create_azure_repo():
    with open("token.txt", "r") as f:
        pat_token = f.read().strip()
    
    organization = ""  # Replace with your org
    project = ""            # Replace with your project
    
    encoded_pat = base64.b64encode(f":{pat_token}".encode()).decode()
    url = f"https://dev.azure.com/{organization}/{project}/_apis/git/repositories?api-version=6.0"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {encoded_pat}"
    }
    data = {"name": "Proj_calc"}
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        repo_url = response.json()["remoteUrl"]
        with open("repo_url.txt", "w") as f:
            f.write(repo_url)
        print(f"Repository created: {repo_url}")
        return repo_url
    else:
        raise Exception(f"Repo creation failed: {response.status_code} - {response.text}")