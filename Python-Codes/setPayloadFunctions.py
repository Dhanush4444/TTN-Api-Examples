import time
import ttn

app_id = ""
access_key = ""

# client.set_custom_payload_functions(encoder="", 
# decoder="", validator="", converter="")

# Arguments left empty are ignored and won’t be updated.

decoder_fn = """function Decoder(payload) {
   return { value: 0 };
}"""

handler = ttn.HandlerClient(app_id, access_key)

app_client =  handler.application()
client.set_custom_payload_functions(decoder=decoder_fn)
