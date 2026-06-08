import requests
import os
import base64
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get GitHub token from .env
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Every request to GitHub needs this header
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}


def parse_github_url(url: str):
    # Remove trailing slash if any
    url = url.rstrip("/")
    # Split URL into parts
    parts = url.split("/")
    # Extract owner and repo name
    owner = parts[-2]
    repo = parts[-1]
    return owner, repo


def get_repo_files(owner: str, repo: str):
    # Build GitHub API URL
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/main?recursive=1"
    
    # Call GitHub API
    response = requests.get(url, headers=HEADERS)
    
    # Convert response to Python readable format
    data = response.json()
    
    # Get only files, skip folders
    files = [
        item["path"] for item in data["tree"]
        if item["type"] == "blob"
    ]
    
    return files


def get_file_content(owner: str, repo: str, file_path: str):
    # Build GitHub API URL for specific file
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    
    # Call GitHub API
    response = requests.get(url, headers=HEADERS)
    
    # Convert response to Python readable format
    data = response.json()
    
    # Decode from Base64 to readable text
    content = base64.b64decode(data["content"]).decode("utf-8")
    
    return content