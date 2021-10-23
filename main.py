import socket
import time
import os

from dotenv import load_dotenv
from fastapi import FastAPI
import requests

app = FastAPI()
#ec2Ip = "http://3.21.169.95"  # DBF ec2 ip, Put into .env
ec2Ip = "http://3.144.155.72:8000/printerip/" # Personal ec2 ip for testing
print(requests.get(ec2Ip))

load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
sleepTime = int(os.getenv('sleepTime'))

while True:
    stream = os.popen('hostname -I')
    localIp = stream.readlines()
    localIp = localIp.replace('[', '')
    localIp = localIp.replace(']', '')
    localIp = localIp.replace('\n', '')
    localIp = localIp.replace(' ', '')
    requests.get(ec2Ip + str(localIp) + '?')
    time.sleep(sleepTime)
