import sys
import paho.mqtt.client as paho
import time
import keyboard 
import threading

username    = "Vahid"
password    = "Rostami"
portal_id   = "your VRM portal ID"
mqtt_broker = "127.0.0.1" #"mqtt67.victronenergy.com"
Port_id     = 1883
# topicIoT1    = "1"

topic_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12" ,"13", "14", "15"]


client = paho.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    for item in topic_list:
        client.subscribe(item)

# The callback for when a PUBLISH message is received from the server.

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    Str = f"{msg.payload.decode()}"
    print(f"msg.payload.decode() from sensor number {msg.topic}: " + Str) 
       

def Connect():
    if client.connect(mqtt_broker, Port_id, 60) != 0:
        print("Couldn't connect to the mqtt broker  !!!!! ")
        sys.exit(1)
    print("Client is connected to the mqtt broker .... ")   
    #subscribe(client)
def DataRecieved():
    DataFlag =0
    print('thread is runing  .... ',DataFlag )
    global client
    while(client.loop()==0):       
            time.sleep(0.2)

    exit(0) 
        
def DataSend():
        Kflag=True
        return
        Str= input("Enter a test : ")
        if(len(Str)<2):
            client.disconnect()
            exit(0)
        for item in topic_list:
            client.publish(item, f"Vahid Client number {item}"+Str, 0)

client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username, password)

Connect()
DataFlag =0
#receiveThread = threading.Thread(target = DataRecieved, args = (DataFlag, True))
receiveThread = threading.Thread(target = DataRecieved)
receiveThread.start()

print("ESC quittt")
client.loop()
while True:
        if keyboard.is_pressed(chr(27)):
            print("ESC quit")
            break
        if keyboard.is_pressed(' '):
                sensor_id = input("Enter Sensor you want to send data : ").strip() 
                while sensor_id not in topic_list:
                    sensor_id = input("Enter Sensor you want to send data : ").strip()
                Str= input("Enter a test : ")
                if(len(Str)<4):
                 break
                client.publish(str(sensor_id), "Vahid Client: "+Str, 0)
                # client.publish(str(sensor_id), f"Vahid Client number {sensor_id}")
                # for item in topic_list:
                #     client.publish(item, "Vahid Client number {item}: "+Str, 0)
        
        
        #time.sleep(0.5)
print("Disconnecting from the MQTT broker")
client.disconnect()
exit(0)
#except Exception:
#        print("Caught an Exception, something went wrong...")
exit(0)        
try:  
     while(1):

       if keyboard.read_key() == 'enter':
         print("Enter is pressed")
       else:
         print("Enter is pressed")
         client.loop() 
         time.sleep(0.2)

except Exception:
        print("Caught an Exception, something went wrong...")
finally:
      print("Disconnecting from the MQTT broker")
      #client.disconnect()


if __name__ == '__main__':
    run()
    client.disconnect()
