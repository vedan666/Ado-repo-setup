```markdown
# Automated Azure Repo & Terraform Structure Setup

This project automates the creation of an Azure DevOps repository, generates a predefined Terraform folder structure, and pushes it to the new repository. Perfect for quickly setting up standardized IaC projects.

## Prerequisites
- Python 3.8+
- Git installed
- Azure DevOps account
- Personal Access Token (PAT) with repo read/write permissions

## Setup
1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/terraform-automation-scripts.git
   cd terraform-automation-scripts
   ```

2. **Create `token.txt`**
   - Place your Azure PAT in a file named `token.txt` in the root directory
   - ⚠️ **Never commit this file!**

## Script Components
| File                   | Purpose                                                                 |
|------------------------|-------------------------------------------------------------------------|
| `main.py`              | Main controller that runs all steps in sequence                        |
| `create_repo.py`       | Creates "Proj_calc" repository in Azure DevOps                         |
| `clone_repo.py`        | Clones the empty repository to your local machine                      |
| `create_folder_structure.py` | Builds Terraform folders/files directly in cloned repo              |
| `git_operations.py`    | Commits changes and pushes to Azure DevOps                             |

## Workflow
1. **Create Repository**  
   Uses your PAT to tell Azure DevOps:  
   _"Make a new empty repo called Proj_calc!"_

2. **Clone Repository**  
   Downloads the empty repo to a folder named `Proj_calc` on your computer.

3. **Generate Structure**  
   Builds these folders/files inside `Proj_calc`:
   ```
   /environment
     /dev, /qa, /prod
       main.tf, variables.tf, provider.tf, terraform.tf
   /modules
     /resource_group
       main.tf, output.tf, variables.tf
   ```

4. **Commit & Push**  
   Saves all changes and uploads them to Azure DevOps.

## Usage
Run the entire process:
```bash
python main.py
```

## Customization
1. **Change Repo/Project Name**  
   Edit these values in `create_repo.py`:
   ```python
   organization = "your-organization"  # Azure DevOps org
   project = "your-project"            # Azure DevOps project
   ```

2. **Modify Folder Structure**  
   Update `create_folder_structure.py` to add/remove folders or files.

## Troubleshooting
| Error                          | Solution                                |
|--------------------------------|-----------------------------------------|
| "Permission denied"            | Ensure PAT in `token.txt` has repo permissions |
| "Repository already exists"    | Delete existing repo in Azure DevOps    |
| "Empty repository" warning     | Ignore - expected for first-time setup  |

## Security
- Add `token.txt` to `.gitignore` to prevent accidental exposure
- PAT should have minimal required permissions (repo read/write)

```

---

### How to Use This README:
1. Save this as `README.md` in your project root
2. Update the "Customization" section if you modify the scripts
3. Commit it to your repository for future reference

This documentation helps users understand:  
✅ **What the scripts do**  
✅ **How to set them up**  
✅ **How to troubleshoot**  
✅ **Security best practices**