import os
import requests

# Destination folder
DATA_DIR = "data/raw"
os.makedirs(DATA_DIR, exist_ok=True)

# Placeholder file (simulate download)
url = "https://www.cms.gov/medicare-coverage-database/downloads/ncd.zip"
dest_path = os.path.join(DATA_DIR, "ncd.zip")

def download_ncd():
    print(f"📥 Downloading NCD data from {url}")
    response = requests.get(url)
    with open(dest_path, "wb") as f:
        f.write(response.content)
    print(f"✅ Saved to {dest_path}")

if __name__ == "__main__":
    download_ncd()
