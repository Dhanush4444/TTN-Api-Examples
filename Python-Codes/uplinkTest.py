import time
import ttn

app_id = "m"
access_key = ""

def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)
  print(msg)

def connect_callback(res,client):
    if res == True:
        print('Connection Successfull')
    else:
        print('Connection Failed')


handler = ttn.HandlerClient(app_id, access_key)
mqtt_client = handler.data()
mqtt_client.connect()
mqtt_client.set_connect_callback(connect_callback)

mqtt_client.close()
