import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moviendo un círculo con Pygame")

# Cargar la imagen de fondo
background = pygame.image.load("../imagenes/background_image.jpg")
background = pygame.transform.scale(background, (width, height))

# Definir los colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Definir las propiedades del círculo
circle_radius = 25
circle_x = width // 2
circle_y = height // 2
circle_speed = 15  # Aumentar la velocidad del círculo

# Función para mover el círculo
def move_circle(keys):
    global circle_x, circle_y

    if keys[pygame.K_LEFT]:
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT]:
        circle_x += circle_speed
    if keys[pygame.K_UP]:
        circle_y -= circle_speed
    if keys[pygame.K_DOWN]:
        circle_y += circle_speed

    # Si el círculo sale de la pantalla, aparece por el lado opuesto
    if circle_x > width + circle_radius:
        circle_x = -circle_radius
    elif circle_x < -circle_radius:
        circle_x = width + circle_radius
    if circle_y > height + circle_radius:
        circle_y = -circle_radius
    elif circle_y < -circle_radius:
        circle_y = height + circle_radius

# Loop principal
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener el estado de las teclas
    keys = pygame.key.get_pressed()

    # Mover el círculo
    move_circle(keys)

    # Dibujar la imagen de fondo y el círculo
    screen.blit(background, (0, 0))
    pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de la ejecución
    pygame.time.Clock().tick(30)

# Salir del juego
pygame.quit()
sys.exit()
