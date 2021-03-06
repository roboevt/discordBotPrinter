import time
import os
from dotenv import load_dotenv
from fastapi import FastAPI
import requests

load_dotenv()
app = FastAPI()

name = os.getenv('name')
model = os.getenv('model')
ec2Ip = os.getenv('botIp')
sleepTime = int(os.getenv('sleepTime'))

while True:
    stream = os.popen('hostname -I')
    localIp = stream.readlines()[0]
    localIp = localIp.replace('[', '')
    localIp = localIp.replace(']', '')
    localIp = localIp.replace('\n', '')
    localIp = localIp.replace(' ', '')
    try:
        requests.get(f"{ec2Ip}{name},{model},{localIp}")
    except:  # Main discord bot program is not running
        pass  # Nothing to do, just skip this iteration
    time.sleep(sleepTime)
