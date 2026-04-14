import socket
import re
import math

HOST = "challenge01.root-me.org"
PORT = 52002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    data = s.recv(1024).decode()
    print("Received:", data)

    numbers = re.findall(r'\d+', data)
    
    if len(numbers) >= 2:
        a = int(numbers[0])
        b = int(numbers[1])

        result = round(math.sqrt(a) * b, 2)

        s.sendall(str(result).encode())

        response = s.recv(1024).decode()
        print("Server response:", response)
