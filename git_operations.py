import subprocess

def git_add_commit_push(clone_dir):
    # Configure git (use placeholder values)
    subprocess.run(["git", "config", "user.email", "terraform@example.com"], cwd=clone_dir, check=True)
    subprocess.run(["git", "config", "user.name", "Terraform Automation"], cwd=clone_dir, check=True)
    
    # Stage changes
    subprocess.run(["git", "add", "."], cwd=clone_dir, check=True)
    
    # Commit
    try:
        subprocess.run(["git", "commit", "-m", "Initial Terraform structure"], cwd=clone_dir, check=True)
    except subprocess.CalledProcessError:
        print("Nothing to commit")
        return
    
    # Push (use HEAD:main to handle empty repo)
    subprocess.run(["git", "push", "origin", "HEAD:main"], cwd=clone_dir, check=True)
    print("Changes pushed successfully")