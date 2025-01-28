import os

def create_folder_structure_in_repo(clone_dir):
    environments = ["qa", "prod", "dev"]
    modules = ["resource_group"]
    
    # Create environment directories
    for env in environments:
        env_path = os.path.join(clone_dir, "environment", env)
        os.makedirs(env_path, exist_ok=True)
        for file in ["main.tf", "variables.tf", "provider.tf", "terraform.tf"]:
            open(os.path.join(env_path, file), 'w').close()
    
    # Create module directories
    for module in modules:
        module_path = os.path.join(clone_dir, "modules", module)
        os.makedirs(module_path, exist_ok=True)
        for file in ["main.tf", "output.tf", "variables.tf"]:
            open(os.path.join(module_path, file), 'w').close()
    
    print("Folder structure created in repository")