from bluetooth import *

socket = BluetoothSocket(RFCOMM)
socket.connect(("AB:F5:94:56:34:02", 1))
print("bluetooth connected!")

msg = input("RPI->BT DATA:")
socket.send(msg)

print("once TX finished")
socket.close()
