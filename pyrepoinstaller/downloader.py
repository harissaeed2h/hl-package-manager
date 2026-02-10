import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

localRoot = "/home/haris/local_repo/"
onlineRoot = "https://archive.ubuntu.com/"
MAX_WORKERS = 10  # Change this to download X files at once

def download_file(url):
    # Calculate paths
    file_path = url.replace(onlineRoot, localRoot)
    folder_path = os.path.dirname(file_path)

    # Create directory and download
    os.makedirs(folder_path, exist_ok=True)
    
    print(f"Starting: {url}")
    # Using -q to keep the console clean during parallel downloads
    # -P allows us to specify the directory without using os.chdir()
    subprocess.run(["wget", "-q", "-P", folder_path, url])
    print(f"Finished: {url}")

def main():
    if not os.path.exists("links.txt"):
        print("links.txt not found!")
        return

    with open("links.txt") as f:
        urls_list = f.read().split()

    # This is where the magic happens
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(download_file, urls_list)

if __name__ == "__main__":
    main()
