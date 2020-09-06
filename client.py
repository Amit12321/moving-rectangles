import pygame
import player
from network import Network
from pickle import dumps, loads
width, height = 500, 500

window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Client") 

def redraw(window, players):
    window.fill( (255, 255, 255) )
    for p in players.values():
        p.draw(window)
    pygame.display.update()

def main():
    run = True
    n = Network()
    print(n.get_client().recv(2048).decode()) # Choose color message
    color = input()
    n.set_player(n.send(color))
    
    myself = n.get_player()
    print("[CLIENT] Recieved player: ", myself)
    clock = pygame.time.Clock()
    other_players = []
    while run:
        clock.tick(60)
<<<<<<< HEAD
=======
        print("[CLIENT] Starts new loop")
>>>>>>> 1b7bc4129fcf58a8cb31c2527e07944538960e61
        other_players = n.send(myself)
        print("[CLIENT] Recieved other players: ", other_players)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        myself.move()
        redraw(window, other_players)

main()
pygame.quit()        