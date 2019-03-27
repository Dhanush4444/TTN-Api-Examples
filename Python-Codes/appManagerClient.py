import time
import ttn

app_id = ""
access_key = ""

handler = ttn.HandlerClient(app_id, access_key)

app_client =  handler.application()
my_app = app_client.get()
print(my_app)
my_devices = app_client.devices()
print(my_devices)