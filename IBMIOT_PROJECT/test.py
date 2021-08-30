import wiotp.sdk.device
import datetime
import time
import random
myConfig = { 
    "identity": {
        "orgId": "41458d",
        "typeId": "Krishna0607",
        "deviceId":"06072002"
    },
    "auth": {
        "token": "Krishna0607"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    print("\n Person with ID " + str(m) + " should leave the room immediately to avoid radiation")
    print()
    time.sleep(3)

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

name = { 273: 'VARUN', 266: 'HARSHITH', 271: 'SUSWANTH', 279: 'KUNNAM'}
l = [273,266,271,279]
now=datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

while True:
    k = int(input("Enter 5 to refresh/ to receive commands"))
    if k==5:
        client.commandCallback = myCommandCallback
    else:
        i = int(input("\n Enter the Employee ID: "))
        n = input("Enter Employee Name: ")
        if i in l:
            if name[i] == n:
                print("Person is authorized you can enter")
                myData={'id':i, 'name':n,'date_time':date_time}
                client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
                print("Published data Succesfully: %s",myData)
            else:
                print("Invalid name for the Employee ID")
        else:
            print("Unauthorized Access")
    
        client.commandCallback = myCommandCallback
    print()
client.disconnect()

