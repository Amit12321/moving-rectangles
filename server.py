import random
import socket
import struct
from pickle import dumps, loads

import _thread
from player import Player

COLORS_MAP = {
    "RED" : (255, 0, 0),
    "GREEN" : (0, 255, 0),
    "BLUE" : (0, 0, 255)
}

server = "192.168.1.33"
port = 8820
currentPlayer = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(1)

print("[SERVER] Waiting for connections")

players = {}

def threaded_client(conn, p_id):
    conn.send(str.encode("Choose color: RED/GREEN/BLUE"))
    color = loads(conn.recv(2048))

    new_player = Player(random.randrange(0, 400), random.randrange(0, 400), 50, 50, COLORS_MAP[color], 5)
    players[p_id] = new_player

    packet = dumps(new_player)
    length = struct.pack('!I', len(packet))
    packet = length + packet
    print("[SERVER] Sending: ", packet)
    conn.send(packet)

    reply = ""
    while True:
        try:
            data = loads(conn.recv(4096))
            players[p_id] = data
            if not data:
                print("[SERVER] Disconnected")
                break
            else:
                reply = players
                print("[SERVER] Received: ", data)
                print("[SERVER] Sending : ", reply)
            send = dumps(reply)
            length = struct.pack('!I', len(send))
            packet = length + send
            conn.sendall(packet)
        except Exception as e:
            print(e)
            del players[p_id]
            break

    print("[SERVER] Lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("[SERVER] Connected to:", addr)

    _thread.start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
