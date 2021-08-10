import wiotp.sdk.device
import datetime
import time
import random
import threading

myConfig = { 
    "identity": {
        "orgId": "b9uud8",
        "typeId": "Dummy",
        "deviceId":"Dummy123"
    },
    "auth": {
        "token": "abcdef123"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

name = { 273: 'VARUN', 266: 'HARSHITH', 271: 'SUSWANTH', 279: 'KUNNAM'}
now=datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

def Exit_Dummy_Radiation(userName):
  print( userName + " Please Exit Radiation room")
  Dummy_Demo()

def Dummy_Demo():
  print('''You can perform operation
   1. Enter Industry plant
   2. Enter Radiation room
   3. Exit Radiation room
   4. Exit Industry plant ''')

  choice = int(input("Select operation from 1,2,3,4 : "))
  print (switch(choice))

while True:

    def Enter_Indusrty():
        i=int(input("Enter the ID to Enter Indusry Plant: "))
        myData={'id':i, 'name':name[i], 'Date_Time':date_time }
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Published data Succesfully: %s",myData)
        print( name[i]+" Entered Industry Plant")

    def Enter_Radiation():
        j=int(input("Enter the ID to Enter Radiation room: "))
        myData={'id':j, 'name':name[j], 'Date_Time':date_time }
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Published data Succesfully: %s",myData)
        print( name[j]+" Entered Radiation room")
        Dummy_Demo()
        threading.Timer(5.0, Exit_Dummy_Radiation(name[j])).start()
        time.sleep(15)
        
    def Exit_Radiation():
        k=int(input("Enter the ID to Exit Radiation room: "))
        myData={'id':k, 'name':name[k], 'Date_Time':date_time }
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Published data Succesfully: %s",myData)
        print( name[k]+" Exited Radiation room")
        
    def Exit_Industy():
        l=int(input("Enter the ID to Exited Indusry Plant: "))
        myData={'id':l, 'name':name[l], 'Date_Time':date_time }
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Published data Succesfully: %s",myData)
        print( name[l]+" Exited Industry Plant")
    def default():
        print("Selected Choice is not correct")

    switcher = {
        1: Enter_Indusrty,
        2: Enter_Radiation,
        3: Exit_Radiation,
        4: Exit_Industy,
        }

    def switch(operation):
        return switcher.get(operation, default)()

    print('''You can perform operation
    1. Enter Industry plant
    2. Enter Radiation room
    3. Exit Radiation room
    4. Exit Industry plant ''')

    #Take input from user
    choice = int(input("Select operation from 1,2,3,4 : "))
    print (switch(choice))
    
    client.commandCallback = myCommandCallback
    time.sleep(15)
client.disconnect()
{"mode":"full","isActive":false}
