import socket
import rsa

# Connect to server
client = socket.socket()
client.connect(('192.168.1.2', 9999))   # Replace with server IP

# Receive public key
public_key_data = client.recv(1024)
public_key = rsa.PublicKey.load_pkcs1(public_key_data)

# Message to send
message = "Hello Server, this is secure!"

# Encrypt message
encrypted_msg = rsa.encrypt(message.encode(), public_key)

# Send encrypted message
client.send(encrypted_msg)

print("Encrypted message sent!")

client.close()