from bluetooth import *
socket = BluetoothSocket( RFCOMM )
socket.connect(("AB:F5:94:56:34:02", 1))
print("bluetooth connected!")
buffer = ""
while True:
    data = socket.recv(1024)
    buffer += data.decode('utf-8')
    if buffer[-1] == '\r':
        print("BT->RPI:%s" %buffer)
        buffer = ""
    elif(buffer[-1] == '\n'):
        print("Quit")
        break
socket.close()
