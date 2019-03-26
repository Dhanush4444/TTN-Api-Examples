import time
import ttn

app_id = ""
access_key = ""

hexPayload = 'AA'.decode('hex').encode('base64')

def downlinkCallback(mid,obj):
    print(obj)

def connect_callback(res,client):
    if res == True:
        print('Connection Successfull')
    else:
        print('Connection Failed')


handler = ttn.HandlerClient(app_id, access_key)
mqtt_client = handler.data()
mqtt_client.connect()
mqtt_client.set_connect_callback(connect_callback)
mqtt_client.send(dev_id="sensor1",  pay= hexPayload, port=1, conf=False, sched="replace")

mqtt_client.close()
