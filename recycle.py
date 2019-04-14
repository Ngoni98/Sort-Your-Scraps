import sys, pygame
from pynput.keyboard import Key, Listener
import time
import random


high_score_list = [0, 0, 0]

class Background(pygame.sprite.Sprite):
	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location

class Block(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
	def __init__(self, bin_type):
       # Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
		#self.image = pygame.Surface([width, height])
		#self.image.fill(color)
		self.image = pygame.image.load(bin_images[bin_type])
		
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()
		
class Heart(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
	def __init__(self):
       # Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
		#self.image = pygame.Surface([width, height])
		#self.image.fill(color)
		self.image = pygame.image.load("tiny_heat.png")
		
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()

class Trash(pygame.sprite.Sprite):

	trash_type = -1
    # Constructor. Pass in the color of the block,
    # and its x and y position
	def __init__(self, trash_i, image_i):
       # Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
		#self.image = pygame.Surface([width, height])
		#self.image.fill(color)
		self.image = pygame.image.load(garbage_images[trash_i][image_i])

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()
		
		self.trash_type = trash_i

def start_page():
	pygame.mixer.music.load("Menu.ogg")
	pygame.mixer.music.play(-1) # -1 = loop indefinitely 
	
	BackGround = Background('world.png', [0,0])
	BackGround2 = Background('instructions.png', [0,0])
	screen.fill(WHITE)
	screen.blit(BackGround.image, BackGround.rect)
  
	# Welcome message 
	display_text('Welcome!', BLACK, 400, 200, 50)
	display_text('saving the world one', BLACK, 400, 300, 30)
	display_text('small step at a time', BLACK, 400, 340, 30)
  
	# blurb about recycling
	# play game button
	
	instructions = False
	
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()
				
		# not displaying the instructions
		if not instructions:
			
			mouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			key=pygame.key.get_pressed()  #checking pressed keys
			
			if 350+100 > mouse[0] > 350 and 400+50 > mouse[1] > 400:
				pygame.draw.rect(screen, GRAY,(350,400,130,50))
				if click[0]:
					play_game()
					pygame.mixer.music.stop()
			else:
				pygame.draw.rect(screen, WHITE,(350,400,130,50))
				
			display_text('play game', BLACK, (height/2+(130/2)), (width/2+(50/2)), 20)
			
			# add instructions option
			if 350+100 > mouse[0] > 350 and 500+50 > mouse[1] > 500:
				pygame.draw.rect(screen, GRAY,(350,500,130,50))
				if click[0]:
					instructions = True
					screen.fill(WHITE)
					screen.blit(BackGround2.image, BackGround2.rect)
					pygame.display.update()
					time.sleep(0.5)
			else:
				pygame.draw.rect(screen, WHITE,(350,500,130,50))
				
			if not instructions: display_text('instructions', BLACK, (350+(130/2)), (500+(50/2)), 20)
			
			pygame.display.update()
			
		else:
		# display instructions
			click = pygame.mouse.get_pressed()
			key=pygame.key.get_pressed()  #checking pressed keys
			if click[0] or key[pygame.K_RETURN]:
				instructions = False
				screen.fill(WHITE)
				screen.blit(BackGround.image, BackGround.rect)
				display_text('Welcome!', BLACK, 400, 200, 50)
				display_text('saving the world one', BLACK, 400, 300, 30)
				display_text('small step at a time', BLACK, 400, 340, 30)
						
def display_text(txt_str, color, x_loc, y_loc, font_size):
	text_font = pygame.font.Font('freesansbold.ttf', font_size)
	TextSurf = text_font.render(txt_str, True, color)
	TextRect = TextSurf.get_rect()
	TextRect.center = (x_loc, y_loc)
	screen.blit(TextSurf, TextRect)
	
def update_score(score):
	display_text('Score: {}'.format(score), WHITE, 45, 15, 20)
	
def display_lives(lives):
	lives_str = 'Lives: '
	for i in range(lives):
		lives_str += 'X '
	display_text(lives_str, WHITE, 650, 15, 20)
	
def death(score):
	pygame.mixer.music.load("dieded.ogg")
	pygame.mixer.music.play(-1) # -1 = loop indefinitely 
	
	BackGround = Background('badworld.png', [0,0])
	screen.fill(WHITE)
	screen.blit(BackGround.image, BackGround.rect)
	
	fact_i = random.randint(0, len(facts)-1)

	while 1: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()
				
		display_text('oops :(', BLACK, 400, 150, 100)
		display_text('Score: {}'.format(score), BLACK, 400, 300, 35)
		
		display_text(facts[fact_i][0], BLACK, 400, 350, 29)
		display_text(facts[fact_i][1], BLACK, 400, 400, 29)
		display_text('Click anywhere to continue', BLACK, 400, 550, 30)
		pygame.display.flip()
		
		click = pygame.mouse.get_pressed()
		key=pygame.key.get_pressed()  #checking pressed keys
		if click[0] or key[pygame.K_RETURN]:
			high_scores(score)
		
		pygame.display.update()

def high_scores(score):
  
	BackGround = Background('badworld.png', [0,0])
	screen.fill(WHITE)
	screen.blit(BackGround.image, BackGround.rect)
  
	display_text('High Scores:', BLACK, 400, 200, 50)

	changed = 0
	# add score to high_score_list
	if score > high_score_list[0]:
		high_score_list[2] = high_score_list[1]
		high_score_list[1] = high_score_list[0]
		high_score_list[0] = score
		changed = 1
	elif score > high_score_list[1]:
		high_score_list[2] = high_score_list[1]
		high_score_list[1] = score
		changed = 1
	elif score > high_score_list[2]:
		high_score_list[2] = score
		changed = 1

	if changed:
		file = open("high_scores.txt", "w")
		file.write(str(high_score_list[0])+"\n")
		file.write(str(high_score_list[1])+"\n")
		file.write(str(high_score_list[2])+"\n")
		file.close()
	
	# display the scores
	for i in range(3):
		display_text('{}:    {}'.format((i+1),high_score_list[i]), BLACK, 370, 280 + i*40, 40)
	pygame.display.flip()
	time.sleep(.5);
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()
		
		# add play again option
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if 350+100 > mouse[0] > 350 and 400+50 > mouse[1] > 400:
			pygame.draw.rect(screen, GRAY,(350,400,130,50))
			if click[0]:
				pygame.mixer.music.stop()
				play_game()
		else:
			pygame.draw.rect(screen, WHITE,(350,400,130,50))
			
		display_text('play again', BLACK, (350+(130/2)), (400+(50/2)), 20)
		
		pygame.display.update()
	
def play_game():
	pygame.mixer.music.load("PlayGame.ogg")
	pygame.mixer.music.play(-1) # -1 = loop indefinitely 
	
	# BackGround = Background('brick_background.png', [0,0])
	
	# keep track of successes
	score = 0
	lives = 3

	# create the three bins
	all_sprites = pygame.sprite.Group()
	trash_sprites = pygame.sprite.Group()
	bin_list = []
	bin_i = 0
	for i in range(3):
		bin_list.append(Block(i))
		bin_list[i].rect.x = 0
		bin_list[i].rect.y = height - 140
	all_sprites.add(bin_list[bin_i])

	# variables that control the loop
	z_wasnt_pressed = True
	x_wasnt_pressed = True
	# control timing
	current_time = time.clock()
	previous_sprite_time = time.clock()
	new_sprite_interval = 3
	previous_advance_time = time.clock()
	advance_interval = 0.005
	# slow down the arrow key movement
	countFrames = 0
	made_harder = False # has the game been made harder since they last scored?
	speed = 2 # speed of the bins
	#pygame.display.set_caption('Score: {}'.format(score))
	while 1:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()
				
		# CHECK FOR COLLISIONS WITH THE BIN/GROUND
		hit_list = pygame.sprite.spritecollide(bin_list[bin_i], trash_sprites, False)
		for sprite in hit_list:
			# check if it hit the top 
			if sprite.rect.y + 60 - 10 <= bin_list[bin_i].rect.y and sprite.rect.y + 60 + 10 >= bin_list[bin_i].rect.y:
				if sprite.trash_type == bin_i:
					score+= 1
					made_harder = False
					pygame.mixer.Sound("binned.ogg").play(0)
					print('Success!')
				else:
					lives-=1
					pygame.mixer.Sound("Missed.ogg").play(0)
					print('You died!')
			else:
				lives-=1
				print('Missed')
			
			trash_sprites.remove(sprite)
		# if it hit the ground
		for sprite in trash_sprites:
			if sprite.rect.y == height-50:
				lives-=1
				print('You died!')
				pygame.mixer.Sound("Missed.ogg").play(0)
				trash_sprites.remove(sprite)

		key=pygame.key.get_pressed()  #checking pressed keys
		
		# CHANGING BINS (Z AND X)
		if not key[pygame.K_z]:
			z_wasnt_pressed = True
		if not key[pygame.K_x]:
			x_wasnt_pressed = True
		if key[pygame.K_z]and z_wasnt_pressed:
			#pygame.mixer.Sound("change_bin.ogg").play(0)
			current_x = bin_list[bin_i].rect.x	# stores current location
			all_sprites.remove(bin_list[bin_i])	# remove current sprite
			bin_i -= 1
			if bin_i < 0:
				bin_i = 2
			all_sprites.add(bin_list[bin_i])	# add new current sprite
			bin_list[bin_i].rect.x = current_x	# set the right location
			z_wasnt_pressed = False
		
		if key[pygame.K_x]and x_wasnt_pressed:
			#pygame.mixer.Sound("change_bin.ogg").play(0)
			current_x = bin_list[bin_i].rect.x	# stores current location
			all_sprites.remove(bin_list[bin_i])	# remove current sprite
			bin_i += 1
			if bin_i > 2:
				bin_i = 0
			all_sprites.add(bin_list[bin_i])	# add new current sprite
			bin_list[bin_i].rect.x = current_x	# set the right location
			x_wasnt_pressed = False
			
		
		# MOVING THE BIN (LEFT AND RIGHT)
		# if the Left arrow is pressed, move left
		if key[pygame.K_LEFT]:
			if bin_list[bin_i].rect.x > 0:
				bin_list[bin_i].rect.x -= speed
		# if the Left arrow is pressed, move left
		if key[pygame.K_RIGHT]:
			if bin_list[bin_i].rect.x < width-100:
				bin_list[bin_i].rect.x += speed
				
		# TIMING AND INTERVALS
		# if the interval is up, add a new trash sprite
		current_time = time.clock()
		if current_time - previous_sprite_time >= new_sprite_interval:
			previous_sprite_time = current_time
			# add a new trash item
			trash_type = random.randint(0,2)
			trash_item = random.randint(0,len(garbage_images[trash_type])-1)
			t = Trash(trash_type, trash_item)
			t.rect.x = random.randint(0, width-50)
			t.rect.y = 0
			trash_sprites.add(t)
		if current_time - previous_advance_time >= advance_interval:
			previous_advance_time = current_time
			for trash in trash_sprites:
				trash.rect.y += 1
		
		
		
		# DIE IF OUT OF LIVES
		if lives <= 0:
			pygame.mixer.music.stop()
			death(score)
			break
			
		# DIFFICULTY
		if not made_harder and score!=0 and score%2==0:
			if new_sprite_interval > 0.5:
				new_sprite_interval -= 0.1
			if advance_interval > 0.0005:
				advance_interval -= 0.0003
			made_harder = True
			
			if score%10 == 0:
				speed+=1
				if lives < 5:
					lives+=1
				
		
		# REDRAW SCREEN
		screen.fill(NAVY)
		all_sprites.draw(screen)
		trash_sprites.draw(screen)
		update_score(score)
		display_lives(lives)
		pygame.display.flip()
		countFrames += 1
	
pygame.init()

# declare screen variables
size = width, height = [800, 700]
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
LIGHT_YELLOW = (255, 255, 204)
DARK_BLUE = (0, 26, 153)
NAVY = (0, 52, 102)
DARK_GRAY = (64, 64, 64)
PINK = (255, 153, 204)
colors = [RED, GREEN, BLUE]	# change to image files


bin_images = ["bin_trash.png", "bin_recycling.png", "bin_compost.png"]
garbage_images = [["t_bag.png", "t_straw.png"],
["r_bottle.png", "r_coke.png", "r_fountain.png", "r_glass.png"],
["c_cardboard.png", "c_coffee.png", "c_takeout.png", "c_tea.png", "c_towels.png"]]


screen = pygame.display.set_mode(size)

pygame.mixer.init()

file = open("high_scores.txt", "r");

high_score_list[0] = int(file.readline())
high_score_list[1] = int(file.readline())
high_score_list[2] = int(file.readline())

file.close()

facts=[["Every 3 months, Americans throw enough aluminum", "in the landfills to build an entire commercial air fleet."],
["Approximately 1 billion trees worth of paper", "are thrown away every year in the USA."], 
["Plastic bags and garbage thrown into the ocean kill", "as many as 1 million sea creatures every year."],
["A modern glass bottle would take 400 years or more", "to decompose -- and even longer if it's in the landfill."],
["The US is the #1 trash-producing country in the", "world at 1,609 poundsper person per year."], 
["The United States throws away $11.4 billion worth of", "recyclable containers and packaging every year."],
["The amount of plastic film and wrap produced", "annually could shrink-wrap the state of Texas."],
["Aluminum cans make up less than 1% of waste", "in the USA because they are the #1 recycled item"], 
["The majority of the 4 million tons of junk mail that" , "Americans receive annually ends up in landfills."],
["For every 1 ton of paper that's produced, roughly", "300 gallons of oil is used to make it."],
["1 trillion pages of paper is 8.5 million acres of trees." ,"That's an area greater than the state of Maryland."]]

#hearts_group = pygame.sprite.Group()
#hearts_group.add(Heart())

start_page()
