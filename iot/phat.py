#!/usr/bin/python3
# EXECUTE WITH SUPER USER PERMISSIONS!

import envirophat as ep
import json
import requests
import os
import time

def readSensors():
    sensors = {
        "weather": {
            "pressure": float(ep.weather.pressure()),
            "temperature": float(ep.weather.temperature()),
            "altitude": float(ep.weather.altitude()),
        },
        "motion": {
            "accelerometer": list(ep.motion.accelerometer()),
            "heading": float(ep.motion.heading()),
            "magnetometer": list(ep.motion.accelerometer()),
            "raw_heading": float(ep.motion.raw_heading()),
        }
    }

    return sensors

if __name__ == "__main__":
    url = os.environ["ENDPOINT"]
    print("ENDPOINT="+url)

    sensorsJson = json.dumps(readSensors(), sort_keys=True, indent=2)

    print("------")
    print(sensorsJson)

    headers = {'content-type': 'application/json'}
    rjson = requests.post(url, data=sensorsJson, headers=headers)
    print(rjson)
