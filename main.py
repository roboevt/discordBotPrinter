import time
import os
from dotenv import load_dotenv
from fastapi import FastAPI
import requests

load_dotenv()
app = FastAPI()

ec2Ip = os.getenv('botIp')
sleepTime = int(os.getenv('sleepTime'))

while True:
    stream = os.popen('hostname -I')
    localIp = stream.readlines()[0]
    localIp = localIp.replace('[', '')
    localIp = localIp.replace(']', '')
    localIp = localIp.replace('\n', '')
    localIp = localIp.replace(' ', '')
    requests.get(ec2Ip + str(localIp) + '?')
    time.sleep(sleepTime)
