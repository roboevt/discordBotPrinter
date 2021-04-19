import socket
import time
import os

from dotenv import load_dotenv
from github import Github

load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
github = Github(os.getenv('GITHUB_TOKEN'))
repository = github.get_user().get_repo('discordBot')
sleepTime = int(os.getenv('sleepTime'))

while True:
    hostname = socket.gethostname()
    localIp = socket.gethostbyname(hostname)
    contents = repository.get_contents("printerip.txt", ref="development")
    repository.update_file('printerip.txt', 'updated printer ip', str(localIp), contents.sha, branch='development')
    print(f"Updated printer ip to {localIp}")
    time.sleep(sleepTime)
