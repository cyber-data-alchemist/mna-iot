### Call dependencies ####
import os
import pandas as pd
import time
import paho.mqtt.client as mqttClient
from dotenv import load_dotenv
from random import randint
load_dotenv()



### Generate data out of csv ####
path_file = "data.csv"
df = pd.read_csv(path_file, index_col = 0)
df = df.dropna()

temp = df.Temperature.tolist()
hum = df.Humidity.tolist()
co = df.CO2.tolist()



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

# Connection variables
Connected = False
broker_address = os.getenv("BROKER")
port =  int(os.getenv("PORT"))
username = os.getenv("USER")
password = os.getenv("PASSWORD")
tag = os.getenv("TAG")

# Init connection
client = mqttClient.Client("streamer")
client.username_pw_set(username, password)
client.on_connect = on_connect
client.connect(broker_address, port)
client.loop_start()


### Send rows as messages on the client  ###

while Connected != True:
    time.sleep(0.1)
    try:
        for i, j, k in zip(temp, hum, co):
            val1 = f'"Temperature" : {str(i)}'
            val2 = f'"Humidity" : {str(j)}'
            val3 = f'"CO2" : {str(k)}'
            val = "{" + val1 + "," + val2 + "," + val3 + "}"            
            client.publish(tag, val, qos=2)
            wait_time = randint(500, 5000) / 1000.0
            time.sleep(wait_time)

    except KeyboardInterrupt:
        print("Stopped by user")
        client.disconnect()
        client.loop_stop()