import pygame
pygame.init()

screen_width = 800
screen_height = 600
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)

ship1x = 0
ship1y = screen_height/2
ship2x = screen_width - 40
ship2y = (screen_height/2) - 20

ship1x_change = 0 
ship1y_change = 0
ship2x_change = 0 
ship2y_change = 0




screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Neptune")
#background=pygame.image.load("Sketch001.tif")
player_img = pygame.image.load("P2img.png")
wall_img = pygame.image.load("wall.png")
player2_img = pygame.image.load("Player2img.png")
bullet_img= pygame.image.load("Bullet_edit.png")
bullets_1 = []
bullets_2 =[]


#kingdom1 = pygame.image.load("KDedit1.png")
#kingdom2 = pygame.image.load("KDedit2.png")
SP1 = pygame.image.load("SP1.png")
SP2 = pygame.image.load("SP2.png")
SP11 = pygame.image.load("SP11.png")
SP12 = pygame.image.load("SP12.png")
gameexit = False
while not gameexit:
	for event in pygame.event.get():		
		if event.type == pygame.QUIT:
			gameexit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				gameexit = True
			if event.key == pygame.K_w:
				ship1y_change -= 2
				ship1x_change = 0
			if event.key == pygame.K_s:
				ship1y_change += 2
				ship1x_change = 0
			if event.key == pygame.K_a:
				ship1x_change -= 2
				ship1y_change = 0
			if event.key == pygame.K_d:				
				ship1x_change += 2
				ship1y_change = 0
			if event.key==pygame.K_SPACE:
				bullets_1.append([ship1x + 25,ship1y + 10])
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				ship1y_change = 0
				#ship1x_change = 0
			if event.key == pygame.K_s:
				ship1y_change = 0
				#ship1x_change = 0
			if event.key == pygame.K_a:
				ship1x_change = 0
				#ship1y_change = 0
			if event.key == pygame.K_d:				
				ship1x_change = 0
				#ship1y_change = 0
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				ship2y_change -= 2
				ship2x_change = 0
			if event.key == pygame.K_DOWN:
				ship2y_change += 2
				ship2x_change = 0
			if event.key == pygame.K_LEFT:
				ship2x_change -= 2
				ship2y_change = 0
			if event.key == pygame.K_RIGHT:				
				ship2x_change += 2
				ship2y_change = 0
			if event.key == pygame.K_p:
				bullets_2.append([ship2x + 25,ship2y + 10])
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				ship2y_change = 0
				#ship1x_change = 0
			if event.key == pygame.K_DOWN:
				ship2y_change = 0
				#ship1x_change = 0
			if event.key == pygame.K_LEFT:
				ship2x_change = 0
				#ship1y_change = 0
			if event.key == pygame.K_RIGHT:				
				ship2x_change = 0
				#ship1y_change = 0



		
	if ship1x == 0 and 0 <= ship1y <= 600:
		ship1x += 2
	if ship1x == 760 and 0 <= ship1y <= 600:
		ship1x -= 2
	if ship1y == 0 and 0 <= ship1x <= 800:
		ship1y += 2
	if ship1y == 560 and 0 <= ship1x <= 800:
		ship1y -= 2

	if ship2x == 0 and 0 <= ship2y <= 600:
		ship2x += 2
	if ship2x == 760 and 0 <= ship2y <= 600:
		ship2x -= 2
	if ship2y == 0 and 0 <= ship2x <= 800:
		ship2y += 2
	if ship2y == 560 and 0 <= ship2x <= 800:
		ship2y -= 2

		
		
	ship1x += ship1x_change
	ship1y += ship1y_change
	ship2x += ship2x_change
	ship2y += ship2y_change
	
	#screen.blit(background,(0,0))			
	screen.fill(blue)
	screen.blit(wall_img,(screen_width/2,0))
	screen.blit(wall_img,(screen_width/2,350))
	screen.blit(player_img,(ship1x,ship1y))
	screen.blit(player2_img,(ship2x, ship2y))
	screen.blit(SP1,(0,0))
	screen.blit(SP2,(750,550))
	screen.blit(SP11,(60,0))
	screen.blit(SP12,(680,520))
	for b in range(len(bullets_1)):
		bullets_1[b][0] += 10
	for bullet_1 in bullets_1:
		screen.blit(bullet_img,[bullet_1[0], bullet_1[1]])

	for a in range(len(bullets_2)):
		bullets_2[a][0] -= 10
	for bullet_2 in bullets_2:
		screen.blit(bullet_img, [bullet_2[0], bullet_2[1]])

	#screen.blit(kingdom1,(0,492))
	#screen.blit(kingdom2,(720,0))

	pygame.display.update()
			




clock.tick(30)
pygame.quit()
quit()