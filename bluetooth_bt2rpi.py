from bluetooth import *

socket = BluetoothSocket( RFCOMM )
socket.connect(("AB:F5:94:56:34:02", 1))
print("bluetooth connected!")

while True:
    data = socket.recv(1024)
    print("BT->RPI:%s" %data)
    if(data=="exit"):
        print("Quit")
        break

socket.close()
