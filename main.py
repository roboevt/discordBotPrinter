import socket
import time
import os

from dotenv import load_dotenv
from github import Github

load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
github = Github(os.getenv('GITHUB_TOKEN'))
repository = github.get_user().get_repo('discordBotPrinter')
sleepTime = int(os.getenv('sleepTime'))

previousIp = repository.get_contents("printerip.txt").decoded_content.decode()

while True:
    localIp = socket.gethostbyname(socket.gethostname())
    if localIp != previousIp:
        contents = repository.get_contents("printerip.txt")
        repository.update_file('printerip.txt', 'updated printer ip', str(localIp), contents.sha)
        print(f"Updated printer ip to {localIp}")
    previousIP = localIp
    time.sleep(sleepTime)
