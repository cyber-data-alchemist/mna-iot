### Call dependencies ####
import os
import paho.mqtt.client as mqttClient
import time
from dotenv import load_dotenv
load_dotenv()

#### Connect to Broker ####
def on_connect(client, userdata, flags, rc):
    """
    Function to stablish conection to the broker
    """
    if rc == 0:
        print("Logged in to Broker")
        global Connected
        Connected = True
    else:
        print("Connection Trouble...")
    return

def on_message(client, userdata, message):
    """
    Función que recibe los mensajes del broker    
    """
    print(f"Message - {message.topic} : {message.payload}")    
    return

# Connection variables
Connected = False
broker_address = os.getenv("BROKER")
port = int(os.getenv("PORT"))
username = os.getenv("USER")
password = os.getenv("PASSWORD")
tag = os.getenv("TAG")

# Init connection
client = mqttClient.Client("listener")
client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, port)
client.loop_start()

### Read Messages  ###

while Connected != True:
    time.sleep(0.1)
    client.subscribe(tag)
    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Stopped by user")
        client.disconnect()
        client.loop_stop()