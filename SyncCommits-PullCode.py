import os
import subprocess
from github import Github, GithubException

#Configuration
GITHUB_TOKEN = "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" 
GITHUB_REPO = "Lucky-Hero-Vired-Projects/NginxHTMLDeployment"
LOCAL_REPO_PATH = "/usr/share/nginx/NginixHTMLPYTHONDeployment"

# Initialize GitHub API client
try:
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(GITHUB_REPO)
except GithubException as e:
    print(f"Error initializing GitHub client or accessing repository: {e}")
    exit(1)

def get_latest_github_commit():
    try:
        commits = repo.get_commits()
        latest_commit = commits[0].sha
        return latest_commit
    except GithubException as e:
        print(f"Error fetching latest commit from GitHub: {e}")
        exit(1)

def get_latest_local_commit():
    try:
        os.chdir(LOCAL_REPO_PATH)
        result = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error getting latest local commit: {e}")
        exit(1)

def pull_latest_changes():
    try:
        os.chdir(LOCAL_REPO_PATH)
        subprocess.run(["git", "pull"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error pulling latest changes: {e}")
        exit(1)

def main():
    try:
        latest_github_commit = get_latest_github_commit()
        latest_local_commit = get_latest_local_commit()

        print(f"Latest GitHub commit ID: {latest_github_commit}")
        print(f"Latest local commit ID: {latest_local_commit}")
        
        if latest_github_commit != latest_local_commit:
            print("New commit detected. Pulling latest changes...")
            pull_latest_changes()
        else:
            print("Local repository is up to date.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
