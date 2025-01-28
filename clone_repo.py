import subprocess
import shutil
import os
from urllib.parse import urlparse, urlunparse

def clone_repository(repo_url):
    with open("token.txt", "r") as f:
        pat = f.read().strip()
    
    # Clean up existing directory
    clone_dir = "Proj_calc"
    if os.path.exists(clone_dir):
        shutil.rmtree(clone_dir)
    
    # Build authenticated URL
    parsed_url = urlparse(repo_url)
    authed_url = parsed_url._replace(
        netloc=f"dummy:{pat}@{parsed_url.hostname}"
    )
    auth_repo_url = urlunparse(authed_url)
    
    # Clone repository
    subprocess.run(["git", "clone", auth_repo_url, clone_dir], check=True)
    return clone_dir