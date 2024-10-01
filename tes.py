import pygame
import math

banyakRect = 20
# Initializing Pygame
pygame.init()
# clock = pygame.time.Clock()
 
# Initializing surface
screen = pygame.display.set_mode((400,300))
max_width = 400
max_height = 300
scroll_x = 0
scroll_y = 0

# Initializing Color
color = (0,0,255)

running = True

width = 120
height = 40
radius = width /2
initX = 160
initY = 120
border=2
points = [(0, 0),(0, 0),(0,0),(0,0)]
rotate_degree = 10
rect_degree1 = 20
rect_degree2 = 180-rect_degree1

created = 0

rect_surface = pygame.Surface((5000, 5000))
rect_surface.fill((255, 255, 255))

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Continuous scrolling based on mouse movement
        # if event.type == pygame.MOUSEMOTION:
        #     if event.buttons[0]:  # Left mouse button pressed
        #         scroll_x += event.rel[0]
        #         scroll_y += event.rel[1]

    if (created < banyakRect):
        # pygame.draw.circle(rect_surface, color, (initX , initY), radius - border, border)
        for i in range(banyakRect):       
            
            # pygame.draw.lines(rect_surface, color, True, points)
            x = math.floor(radius * math.cos(math.radians(rect_degree1)))
            y = math.floor(radius * math.sin(math.radians(rect_degree1)))
            
            x2 = math.floor(radius * math.cos(math.radians(rect_degree2)))
            y2 = math.floor(radius * math.sin(math.radians(rect_degree2)))
            
            x3 = math.floor(radius * math.cos(math.radians(-rect_degree1)))
            y3 = math.floor(radius * math.sin(math.radians(-rect_degree1)))

            x4 = math.floor(radius * math.cos(math.radians(-rect_degree2)))
            y4 = math.floor(radius * math.sin(math.radians(-rect_degree2)))
            
            points[0] = (initX + x, initY - y)
            points[1] = (initX + x2, initY - y2)
            points[2] = (initX - x3, initY - y3)
            points[3] = (initX - x4, initY - y4)

            print(points)
            temp = (200,200)
            # pygame.draw.lines(rect_surface, color, True, points, border)
            pygame.draw.line(rect_surface, color, points[0], points[1])
            pygame.draw.line(rect_surface, color, points[1], points[2])
            pygame.draw.line(rect_surface, color, points[2], points[3])
            pygame.draw.line(rect_surface, color, points[3], points[0])
            rect_degree1 -= rotate_degree
            rect_degree2 -= rotate_degree

            # titik1 = list(points[0])
            # titik1[0] = center_coorX - x
            # titik1[1] = center_coorY - y
            # points[0] = tuple(titik1)

            # titik2 = list(points[1])
            # titik2[0] = center_coorX + x
            # titik2[1] = center_coorY + y
            # points[1] = tuple(titik2)

            # titik3 = list(points[2])
            # titik3[0] = center_coorX2 - x
            # titik3[1] = center_coorY2 - y
            # points[2] = tuple(titik3)

            # titik4 = list(points[3])
            # titik4[0] = center_coorX2 + x
            # titik4[1] = center_coorY2 + y
            # points[3] = tuple(titik4)



            
            created += 1

            

    screen.blit(rect_surface, (-scroll_x, -scroll_y))
    pygame.display.update()
# Drawing Rectangle
