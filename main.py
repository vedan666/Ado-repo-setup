from create_repo import create_azure_repo
from clone_repo import clone_repository
from create_folder_structure import create_folder_structure_in_repo
from git_operations import git_add_commit_push

def main():
    # Step 1: Create Azure Repo
    repo_url = create_azure_repo()
    
    # Step 2: Clone the empty repository
    clone_dir = clone_repository(repo_url)
    
    # Step 3: Create folder structure directly in cloned repo
    create_folder_structure_in_repo(clone_dir)
    
    # Step 4: Commit and push changes
    git_add_commit_push(clone_dir)

if __name__ == "__main__":
    main()