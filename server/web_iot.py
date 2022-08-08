from sensors.buzzer import buzzer_on
from sensors.LCD import LCD
from sensors.LED import LED_State
from sensors.rfid import rfid
from sensors.servo import servo

# modules Imported from python's library
import socket
import traceback
from threading import Thread
import sys
from time import sleep
import requests

# This function receives the binary input sent from a client
# It then decodes the message and returns it as a string
# The arguments of this function are connection which is the socket connection and the max buffer size 
def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    decodedInput = client_input.decode("utf8").rstrip()
    return decodedInput
    
# This function starts the server
def start_server():
    host = "127.0.0.1"
    port = 8000 # arbitrary non-privileged port
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket created")
    try:
        soc.bind((host, port))
    except:
        print("Bind failed. Error : " + str(sys.exc_info()))
        sys.exit()
    # [Modified] prevents collision of multiple requests on the same socket
    # queue up to 1 requests
    soc.listen(1)
    print("Socket now listening")
    # infinite loop- do not reset for every requests
    while True:
        connection, address = soc.accept()
        ip, port = str(address[0]), str(address[1])
        print('-------------------------------------------------')
        print('\n' + '\33[42m' + "Connected with " + ip + ":" + port + '\33[0m')
        
        try:
            Thread(target=clientThread, args=(connection, ip, port)).start()  # starting of a thread.
        
        except KeyboardInterrupt:  # to stop programme with ctrl + c
            print(f"closing connection to {address}.")
            connection.shutdown(socket.SHUT_RDWR)
            connection.close()
            sys.exit()

        except:
            print("Thread did not start.")
            traceback.print_exc()

# This function is to allow user to open the door remotely 
def remoteUnlock(connection):
    servo("OPEN")
    LCD('Door is unlocked!', '----->')
    resp = requests.post("https://api.thingspeak.com/apps/thingtweet/1/statuses/update?api_key=KP60V4Y3POZWNP19&status=Door+has+been+unlocked!")
    connection.send(b'Sucess')
    sleep(20)
    servo("CLOSED")
    return False   # get out of while True loop of clientThread


# This function is for users to remotely change rfid tag with a button on the website
def registerRFID(connection):
    result = rfid("REGISTER", LCD, buzzer_on, LED_State)  
    if result == "REGISTERED":
        connection.send(b'RFID Registered Success!')
    else: 
        connection.send(b'RFID Registered Failed...')

    sleep(10)
    return False  # get out of while True loop of clientThread

# This function is a thread that the client runs on. It waits for message sent by the client before it does
# different types of processing.
# the arguments of the function are connection, the ip and port associated with the client, and the max
# buffer size of each message. 
def clientThread(connection, ip, port, max_buffer_size = 5120):
    is_active = True
    while is_active:
        connection.send(b'Connected. Stoping main iot_logic')
        client_input = receive_input(connection, max_buffer_size)

        if "--Remote Unlock Door--" in client_input: # For Remote unlock door
            print('\n' + '\33[32m' + f"Client {ip}:{port} is requesting to unlock door remotely" + '\33[0m')
            is_active = remoteUnlock(connection)

        elif "--Register RFID--" in client_input: # for register RFID
            print('\n' + '\33[32m' + f"Client {ip}:{port} is requesting to register new RFID tag" + '\33[0m')
            is_active = registerRFID(connection)
    
    connection.send(b'')

start_server()
    