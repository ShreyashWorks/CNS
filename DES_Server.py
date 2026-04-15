import socket
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import hashlib

# Diffie-Hellman values
p = 23
g = 5

# Server private key
b = 6

# Create socket
server = socket.socket()
server.bind(('0.0.0.0', 9999))
server.listen(1)

print("Server waiting for connection...")
conn, addr = server.accept()
print("Connected to:", addr)

# Receive client's public key
A = int(conn.recv(1024).decode())

# Compute server public key
B = (g ** b) % p
conn.send(str(B).encode())

# Generate shared key
shared_key = (A ** b) % p
print("Shared Key:", shared_key)

# Convert shared key to DES key (8 bytes)
key = hashlib.sha256(str(shared_key).encode()).digest()[:8]

# Receive encrypted message
encrypted_msg = conn.recv(1024)

# Decrypt
cipher = DES.new(key, DES.MODE_ECB)
decrypted = unpad(cipher.decrypt(encrypted_msg), DES.block_size)

print("Decrypted Message:", decrypted.decode())

conn.close()