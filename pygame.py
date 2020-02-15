import pygame

pygame.init()

gamelooplaw = pygame.display.set.mode.((800.600))
pygame.display.set_caption('A racing game')
clock = pygame.time.clock

carUng = pygame.image.load('racecar.png')
def car(x,y):
	gameDisplay.blit(carImg,(x,y))

x = (display_width = 0.4)
y = (display_height = 0.5)

crashed = false

while not crashed:
	for event python.event.get():
		if event.type == pygame.QUIT:
			crashed = True
		print(event)
	gameDisplay.fill(WHITE)
	car(x,y)
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()

