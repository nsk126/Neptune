import pygame

""""from PIL import Image
	image_file = "something.jpg"
im = Image.open(image_file)
print im.size   # return value is a tuple, ex.: (1200, 800)"""

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

font = pygame.font.SysFont(None,25)

wall_img = pygame.image.load("sprites\wall2.png")

Player1 = pygame.image.load("sprites\P2img.png")
Player2 = pygame.image.load("sprites\Player2img.png")

kingdom1 = pygame.image.load("sprites\KDedit3.png")
kingdom2 = pygame.image.load("sprites\KDedit4.png")

Player1v2 = pygame.image.load("sprites\SP1.png")
Player2v2 = pygame.image.load("sprites\SP2.png")

Player1v2R = pygame.transform.rotate(Player1v2,90)
Player2v2R = pygame.transform.rotate(Player2v2,90)

Player1v3 = pygame.image.load("sprites\SP11.png")
Player2v3 = pygame.image.load("sprites\SP12.png")

Player1v3R = pygame.transform.rotate(Player1v3,90)
Player2v3R = pygame.transform.rotate(Player2v3,90)

bullet_img= pygame.image.load("sprites\Bullet_edit.png")

KHB200 = pygame.image.load("sprites\KHB200.png")
KHB190 = pygame.image.load("sprites\KHB190.png")
KHB180 = pygame.image.load("sprites\KHB180.png")
KHB170 = pygame.image.load("sprites\KHB170.png")
KHB160 = pygame.image.load("sprites\KHB160.png")
KHB150 = pygame.image.load("sprites\KHB150.png")
KHB140 = pygame.image.load("sprites\KHB140.png")
KHB130 = pygame.image.load("sprites\KHB130.png")
KHB120 = pygame.image.load("sprites\KHB120.png")
KHB110 = pygame.image.load("sprites\KHB110.png")
KHB100 = pygame.image.load("sprites\KHB100.png")
KHB90 = pygame.image.load("sprites\KHB90.png")
KHB80 = pygame.image.load("sprites\KHB80.png")
KHB70 = pygame.image.load("sprites\KHB70.png")
KHB60 = pygame.image.load("sprites\KHB60.png")
KHB50 = pygame.image.load("sprites\KHB50.png")
KHB40 = pygame.image.load("sprites\KHB40.png")
KHB30 = pygame.image.load("sprites\KHB30.png")
KHB20 = pygame.image.load("sprites\KHB20.png")
KHB10 = pygame.image.load("sprites\KHB10.png")
KHB0 = pygame.image.load("sprites\PHB0.png")

PHB100 = pygame.image.load("sprites\PHB100.png")
PHB90 = pygame.image.load("sprites\PHB90.png")
PHB80 = pygame.image.load("sprites\PHB80.png")
PHB70 = pygame.image.load("sprites\PHB70.png")
PHB60 = pygame.image.load("sprites\PHB60.png")
PHB50 = pygame.image.load("sprites\PHB50.png")
PHB40 = pygame.image.load("sprites\PHB40.png")
PHB30 = pygame.image.load("sprites\PHB30.png")
PHB20 = pygame.image.load("sprites\PHB20.png")
PHB10 = pygame.image.load("sprites\PHB10.png")
PHB0 = pygame.image.load("sprites\PHB0.png")

#bullet_sound = pygame.mixer.Sound("Bullet.mp3")
#background_sound = pygame.mixer.Sound("")

Kingdom_Health1 = 200
Kingdom_Health2 = 200

Player1_Health = 100
Player2_Health = 100

wall1x = wall2x = (screen_width/2) - 25
wall1y = 0
wall2y = screen_height - 250

bullets_1 = []
bullets_2 =[]

bullet_speed = 1

gameexit = False
gamepause = False

while not gameexit:

	#Screen Boundaries
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

	#Kingdom boundaries
	if ship1x == 80 and 452 <= ship1y <= 600:
		ship1x += 2
	if ship1y == 452 and 0 <= ship1x <= 80:
		ship1y -= 2
	if ship2x == 80 and 452 <= ship2y <= 600:
		ship2x += 2
	if ship2y == 452 and 0 <= ship2x <= 80:
		ship2y -= 2

	if ship1x == 680 and 0 <= ship1y <= 108:
		ship1x -= 2
	if ship1y == 108 and 680 <= ship1x <= 800:
		ship1y += 2
	if ship2x == 680 and 0 <= ship2y <= 108:
		ship2x -= 2
	if ship2y == 108 and 680 <= ship2x <= 800:
		ship2y += 2

	if ship1x >= wall1x - 40 and wall1y <= ship1y <= wall1y + 250:
		ship1x -= 2
	#print ship1x

	ship1x += ship1x_change
	ship1y += ship1y_change

	ship2x += ship2x_change
	ship2y += ship2y_change

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameexit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				gameexit = True
			#pause command
			if event.key == pygame.K_c:
				if gamepause == False:
					gamepause = True
				else:
					gamepause = False
			if gamepause == False:
				#Player1 movement
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


				#Player2 Movement
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
					bullets_2.append([ship2x+25,ship2y+10])

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




		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				ship2y_change = 0
				#ship2x_change = 0
			if event.key == pygame.K_DOWN:
				ship2y_change = 0
				#ship2x_change = 0
			if event.key == pygame.K_LEFT:
				ship2x_change = 0
				#ship2y_change = 0
			if event.key == pygame.K_RIGHT:
				ship2x_change = 0
				#ship2y_change = 0

	



	#Standard ScreenBlit
	screen.fill(blue)
	screen.blit(wall_img,(wall1x,wall1y))
	screen.blit(wall_img,(wall2x,wall2y))
	screen.blit(kingdom1,(0,492))
	screen.blit(kingdom2,(720,0))

	#ShipScreenBlit for given health
	#Player1
	if Player1_Health >= 70:
		screen.blit(Player1v2,(0,0))
		screen.blit(Player1v3,(60,0))
		screen.blit(Player1,(ship1x,ship1y))
	if 40 <= Player1_Health < 70:
		screen.blit(Player1v3,(60,0))
		screen.blit(Player1v2R,(ship1x,ship1y))
	if 0 <= Player1_Health < 40:
		screen.blit(Player1v3R,(ship1x,ship1y))
	#Player2
	if Player2_Health >= 70:
		screen.blit(Player2v2,(750,550))
		screen.blit(Player2v3,(680,520))
		screen.blit(Player2,(ship2x,ship2y))
	if 40 <= Player2_Health < 70:
		screen.blit(Player2v2R,(ship2x,ship2y))
		screen.blit(Player2v3,(680,520))
	if 0 <= Player2_Health < 40:
		screen.blit(Player2v3R,(ship2x,ship2y))




	if Kingdom_Health1 == 200:
		screen.blit(KHB200,(150,40))

	#for r in range(0,200):
	#	for r in range(190,200):
	#		screen.blit(KHB190,(460,540))

	if 190 <= Kingdom_Health1 < 200:
		screen.blit(KHB190,(150,40))
	if 180 <= Kingdom_Health1 < 190:
		screen.blit(KHB180,(150,40))
	if 170 <= Kingdom_Health1 < 180:
		screen.blit(KHB170,(150,40))
	if 160 <= Kingdom_Health1 < 170:
		screen.blit(KHB160,(150,40))
	if 150 <= Kingdom_Health1 < 160:
		screen.blit(KHB150,(150,40))
	if 140 <= Kingdom_Health1 < 150:
		screen.blit(KHB140,(150,40))
	if 130 <= Kingdom_Health1 < 140:
		screen.blit(KHB130,(150,40))
	if 120 <= Kingdom_Health1 < 130:
		screen.blit(KHB120,(150,40))
	if 110 <= Kingdom_Health1 < 120:
		screen.blit(KHB110,(150,40))
	if 100 <= Kingdom_Health1 < 110:
		screen.blit(KHB100,(150,40))
	if 90 <= Kingdom_Health1 < 100:
		screen.blit(KHB90,(150,40))
	if 80 <= Kingdom_Health1 < 90:
		screen.blit(KHB80,(150,40))
	if 70 <= Kingdom_Health1 < 80:
		screen.blit(KHB70,(150,40))
	if 60 <= Kingdom_Health1 < 70:
		screen.blit(KHB60,(150,40))
	if 50 <= Kingdom_Health1 < 60:
		screen.blit(KHB50,(150,40))
	if 40 <= Kingdom_Health1 < 50:
		screen.blit(KHB40,(150,40))
	if 30 <= Kingdom_Health1 < 40:
		screen.blit(KHB30,(150,40))
	if 20 <= Kingdom_Health1 < 30:
		screen.blit(KHB20,(150,40))
	if 0 < Kingdom_Health1 < 20:
		screen.blit(KHB10,(150,40))
	if Kingdom_Health1 <= 0:
		screen.blit(KHB0,(150,40))

	if Kingdom_Health2 == 200:
		screen.blit(KHB200,(460,540))
	if 190 <= Kingdom_Health2 < 200:
		screen.blit(KHB190,(460,540))
	if 180 <= Kingdom_Health2 < 190:
		screen.blit(KHB180,(460,540))
	if 170 <= Kingdom_Health2 < 180:
		screen.blit(KHB170,(460,540))
	if 160 <= Kingdom_Health2 < 170:
		screen.blit(KHB160,(460,540))
	if 150 <= Kingdom_Health2 < 160:
		screen.blit(KHB150,(460,540))
	if 140 <= Kingdom_Health2 < 150:
		screen.blit(KHB140,(460,540))
	if 130 <= Kingdom_Health2 < 140:
		screen.blit(KHB130,(460,540))
	if 120 <= Kingdom_Health2 < 130:
		screen.blit(KHB120,(460,540))
	if 110 <= Kingdom_Health2 < 120:
		screen.blit(KHB110,(460,540))
	if 100 <= Kingdom_Health2 < 110:
		screen.blit(KHB100,(460,540))
	if 90 <= Kingdom_Health2 < 100:
		screen.blit(KHB90,(460,540))
	if 80 <= Kingdom_Health2 < 90:
		screen.blit(KHB80,(460,540))
	if 70 <= Kingdom_Health2 < 80:
		screen.blit(KHB70,(460,540))
	if 60 <= Kingdom_Health2 < 70:
		screen.blit(KHB60,(460,540))
	if 50 <= Kingdom_Health2 < 60:
		screen.blit(KHB50,(460,540))
	if 40 <= Kingdom_Health2 < 50:
		screen.blit(KHB40,(460,540))
	if 30 <= Kingdom_Health2 < 40:
		screen.blit(KHB30,(460,540))
	if 20 <= Kingdom_Health2 < 30:
		screen.blit(KHB20,(460,540))
	if 0 < Kingdom_Health2 < 20:
		screen.blit(KHB10,(460,540))
	if Kingdom_Health2 <= 0:
		screen.blit(KHB0,(460,540))

	if Player1_Health == 100:
		screen.blit(PHB100,(150,20))
	if 90 <= Player1_Health < 100:
		screen.blit(PHB90,(150,20))
	if 80 <= Player1_Health < 90:
		screen.blit(PHB80,(150,20))
	if 70 <= Player1_Health < 80:
		screen.blit(PHB70,(150,20))
	if 60 <= Player1_Health < 70:
		screen.blit(PHB60,(150,20))
	if 50 <= Player1_Health < 60:
		screen.blit(PHB50,(150,20))
	if 40 <= Player1_Health < 50:
		screen.blit(PHB40,(150,20))
	if 30 <= Player1_Health < 40:
		screen.blit(PHB30,(150,20))
	if 20 <= Player1_Health < 30:
		screen.blit(PHB20,(150,20))
	if 0 < Player1_Health < 20:
		screen.blit(PHB10,(150,20))
	if Player1_Health <= 0:
		screen.blit(PHB0,(150,20))

	if Player2_Health == 100:
		screen.blit(PHB100,(460,560))
	if 90 <= Player2_Health < 100:
		screen.blit(PHB90,(460,560))
	if 80 <= Player2_Health < 90:
		screen.blit(PHB80,(460,560))
	if 70 <= Player2_Health < 80:
		screen.blit(PHB70,(460,560))
	if 60 <= Player2_Health < 70:
		screen.blit(PHB60,(460,560))
	if 50 <= Player2_Health < 60:
		screen.blit(PHB50,(460,560))
	if 40 <= Player2_Health < 50:
		screen.blit(PHB40,(460,560))
	if 30 <= Player2_Health < 40:
		screen.blit(PHB30,(460,560))
	if 20 <= Player2_Health < 30:
		screen.blit(PHB20,(460,560))
	if 0 < Player2_Health < 20:
		screen.blit(PHB10,(460,560))
	if Player2_Health <= 0:
		screen.blit(PHB0,(460,560))

	for b in range (len(bullets_1)):
		bullets_1[b][0] += bullet_speed
		screen.blit(bullet_img,[bullets_1[b][0], bullets_1[b][1]])
		#print bullets_1[0]
		#print Kingdom_Health2

	for x in bullets_1:
		if x[0] >= 700 and 0 <= x[1] <= 108:
			bullets_1.remove(x)
			Kingdom_Health2 -= 2
			Kingdom_Health1 += 1
			if Kingdom_Health1 > 200:
				Kingdom_Health1 = 200
			if Kingdom_Health2 < 0:
				Kingdom_Health2 = 0
		if x[0] >= 800:
			bullets_1.remove(x)
		if x[0]  == ship2x and ship2y <= x[1] <= ship2y + 40:
			bullets_1.remove(x)
			Player2_Health -= 2
			if Player2_Health < 0:
				Player2_Health = 0

	for a in range(len(bullets_2)):
		bullets_2[a][0] -= bullet_speed
		screen.blit(bullet_img, [bullets_2[a][0], bullets_2[a][1]])

	for y in bullets_2:
		if y[0] <= 80 and 492 <= y[1] <= 600:
			bullets_2.remove(y)
			Kingdom_Health1 -= 2
			Kingdom_Health2 += 1
			if Kingdom_Health2 > 200:
				Kingdom_Health2 = 200
			if Kingdom_Health1 < 0:
				Kingdom_Health1 = 0
		if y[0] < 0:
			bullets_2.remove(y)
		if y[0]  == ship1x + 40 and ship1y <= y[1] <= ship1y + 40:
			bullets_2.remove(y)
			Player1_Health -= 2
			if Player1_Health < 0:
				Player1_Health = 0

	KH1Number=str(Kingdom_Health1)
	KH2Number=str(Kingdom_Health2)
	PH1Number=str(Player1_Health)
	PH2Number=str(Player2_Health)

	KH1N=font.render(KH1Number,True,white)
	KH2N=font.render(KH2Number,True,white)
	PH1N=font.render(PH1Number,True,white)
	PH2N=font.render(PH2Number,True,white)

	screen.blit(PH1N,[320,20])
	screen.blit(PH2N,[630,560])
	screen.blit(KH1N,[320,40])
	screen.blit(KH2N,[630,540])

	#pause function
	if gamepause == True:
		ship1x_change = 0
		ship1y_change = 0
		ship2x_change = 0
		ship2y_change = 0
		bullet_speed = 0
		screen.fill(white)

	if gamepause == False:
		bullet_speed = 1

	pygame.display.update()


clock.tick(30)
pygame.quit()
quit()
