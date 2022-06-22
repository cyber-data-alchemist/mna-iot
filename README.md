# MQTT Example
File with a publisher and a listener for an MQTT based on port 1883. This only considers user and password, to include SSL you will need to add more instructions.

To init create a .ENV file with:
* BROKER=
* USER=
* PASSWORD=
* PORT=
* TAG=

Configure the user and password on the host server and run (usually mosquitto) and then run pub.py to start emmit the messages from the censors in the data.csv and then run in other terminal the sub.py to see the messages.