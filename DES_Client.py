import socket
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import hashlib

# Diffie-Hellman values
p = 23
g = 5

# Client private key
a = 15

client = socket.socket()
client.connect(('192.168.1.2', 9999))  # replace with server IP

# Compute public key
A = (g ** a) % p
client.send(str(A).encode())

# Receive server public key
B = int(client.recv(1024).decode())

# Generate shared key
shared_key = (B ** a) % p
print("Shared Key:", shared_key)

# Convert to DES key
key = hashlib.sha256(str(shared_key).encode()).digest()[:8]

# Message to send
message = input("Enter message: ")

# Encrypt
cipher = DES.new(key, DES.MODE_ECB)
encrypted_msg = cipher.encrypt(pad(message.encode(), DES.block_size))

# Send encrypted message
client.send(encrypted_msg)

client.close()