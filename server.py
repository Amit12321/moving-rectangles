import socket
import _thread
from pickle import dumps, loads
from player import Player
import random

COLORS_MAP = {
    "RED" : (255, 0, 0),
    "GREEN" : (0, 255, 0),
    "BLUE" : (0, 0, 255)
}

server = "192.168.1.36"
port = 8820
currentPlayer = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(2)
print("[SERVER] Waiting for connections")

players = []
def threaded_client(conn, p_id):
    conn.send(str.encode("Choose color: RED/GREEN/BLUE"))
    color = loads(conn.recv(2048))
    new_player = Player(random.randrange(0, 500), random.randrange(0, 500), 50, 50, COLORS_MAP[color], 5)
    players.append(new_player)
    conn.send(dumps(new_player))
    reply = ""
    while True:
        try:
            data = loads(conn.recv(4096*2))
            players[p_id] = data
            if not data:
                print("[SERVER] Disconnected")
                break
            else:
                reply = [players[i] for i in range(currentPlayer) if i != p_id]
                print("[SERVER] Received: ", data)
                print("[SERVER] Sending : ", reply)
            conn.sendall(dumps(reply))
        except:
            break

    print("[SERVER] Lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("[SERVER] Connected to:", addr)

    _thread.start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1