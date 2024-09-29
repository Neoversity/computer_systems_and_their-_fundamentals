import socket
import json
from datetime import datetime
from pymongo import MongoClient

def start_socket_server(host='localhost', port=5000):
    client = MongoClient('localhost', 27017)
    db = client['messages_db']
    collection = db['messages']

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Socket server listening on {host}:{port}")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                print(f"Received data: {data}")  # Додаємо виведення отриманих даних
                if data:
                    try:
                        message_dict = json.loads(data.decode('utf-8'))
                        message_dict['date'] = str(datetime.now())
                        collection.insert_one(message_dict)
                        conn.sendall(b"Message received and stored")
                    except json.JSONDecodeError as e:
                        print(f"JSON decode error: {e}")
                        conn.sendall(b"Invalid data format")
                else:
                    conn.sendall(b"No data received")

if __name__ == '__main__':
    start_socket_server()
