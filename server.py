import socket
import rsa

# Generate RSA keys
(public_key, private_key) = rsa.newkeys(1024)

# Create socket
server = socket.socket()
server.bind(('0.0.0.0', 9999))
server.listen(1)

print("Server is waiting for connection...")

conn, addr = server.accept()
print(f"Connected to {addr}")

# Send public key to client
conn.send(public_key.save_pkcs1())

# Receive encrypted message
encrypted_msg = conn.recv(1024)

# Decrypt message
decrypted_msg = rsa.decrypt(encrypted_msg, private_key)

print("Encrypted message:", encrypted_msg)
print("Decrypted message:", decrypted_msg.decode())

conn.close()