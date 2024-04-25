import pygame
import random
import sys

# Pygame setup
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
speed = 15

font = pygame.font.SysFont('Arial', 18)

def map_value(value, leftMin, leftMax, rightMin, rightMax):
    # Maps a value from one range to another
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

class Star:
    def __init__(self):
        self.x = random.uniform(-width / 2, width / 2)
        self.y = random.uniform(-height / 2, height / 2)
        self.z = random.uniform(0, width)
        self.pz = self.z

    def update(self):
        global speed
        self.z -= speed
        if self.z < 1:
            self.z = width
            self.x = random.uniform(-width / 2, width / 2)
            self.y = random.uniform(-height / 2, height / 2)
            self.pz = self.z

    def show(self):
        sx = map_value(self.x / self.z, 0, 1, width / 2, width)
        sy = map_value(self.y / self.z, 0, 1, height / 2, height)

        # Increase line length by adjusting previous position more significantly
        px = map_value(self.x / (self.pz * 1.5), 0, 1, width / 2, width)
        py = map_value(self.y / (self.pz * 1.5), 0, 1, height / 2, height)
        self.pz = self.z

        pygame.draw.line(screen, (255, 255, 255), (int(px), int(py)), (int(sx), int(sy)), 2)

def display_instructions():
    instructions = "Increase speed: Up Arrow | Decrease speed: Down Arrow"
    text = font.render(instructions, True, (255, 255, 255))
    screen.blit(text, (10, 10))

# Create a denser list of stars
stars = [Star() for _ in range(300)]  # Increase number for more density

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed += 1
            elif event.key == pygame.K_DOWN:
                speed -= 1 if speed > 1 else 0

    screen.fill((0, 0, 0))

    for star in stars:
        star.update()
        star.show()

    display_instructions()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
