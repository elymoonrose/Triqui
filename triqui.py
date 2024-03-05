import pygame

# display y nombre del juego
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Triqui")

# imágenes usadas para construir el juego
fondo = pygame.image.load("static/triquiBG.png")
circulo = pygame.image.load("static/triquiO.png")
equis = pygame.image.load("static/triquiX.png")

# tamaño del fondo, circulo y equis
fondo = pygame.transform.scale(fondo, (600, 600))
circulo = pygame.transform.scale(circulo, (120, 120))
equis = pygame.transform.scale(equis, (120, 120))

# coordenadas donde se van a graficar las imágenes usadas
coor = [[(80, 45), (230, 45), (355, 45)],
        [(80, 220), (230, 220), (355, 220)],
        [(80, 400), (230, 400), (355, 400)]]

# matríz para registrar las jugadas realizadas
tablero = [["", "", ""], 
                ["", "", ""], 
                ["", "", ""]]

# turno de jugadores
turno = "x"
game_over = False
tiempo = pygame.time.Clock()


def graficar_board():
    screen.blit(fondo, (0, 0))
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == "x":
                dibujar_x(fila, col)
            elif tablero[fila][col] == "o":
                dibujar_o(fila, col)


def dibujar_x(fila, col):
    screen.blit(equis, coor[fila][col])


def dibujar_o(fila, col):
    screen.blit(circulo, coor[fila][col])


def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != '':
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != '':
            return True
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
            return True
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
            return True
    return False


# loop del juego
while not game_over:
    tiempo.tick(30)
# esta funcion capturará todos los eventos que se hayan registrado durante la iteración anterior
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            if (mouseX >= 80 and mouseX < 495) and (mouseY >= 45 and mouseY < 460):
                fila = (mouseY - 40) // 140
                col = (mouseX - 75) // 140
                if tablero[fila][col] == '':
                    tablero[fila][col] = turno
                    fin_juego = verificar_ganador()
                    if fin_juego:
                        print(f"El jugador {turno} ha ganado!")
                        game_over = True
                    turno = "o" if turno == "x" else "x"

    graficar_board()
    pygame.display.update()

pygame.quit()
