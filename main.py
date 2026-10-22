import pygame
import random

pygame.init()
pygame.display.set_caption("Flappy Bird") #sets the window title
screen = pygame.display.set_mode((400,600)) #creates window

background=pygame.image.load("assets/sprites/background-day.png")
background=pygame.transform.scale(background,(400,600))

ground=pygame.image.load("assets/sprites/base.png")
ground=pygame.transform.scale(ground,(400,70))
# screen.blit(background, (0, 0)) # Draw the background onto the screen
# pygame.display.flip() # Update the display   

bird=pygame.image.load("assets/sprites/redbird-midflap.png")
bird=pygame.transform.scale(bird,(40,30))
bird_x=50
bird_y=250

ground_x=0
ground_y=530

# screen.blit(bird,(bird_x,bird_y))
# pygame.display.flip()

bird_velocity=0
gravity=0.025
jump_strength=-2

background_x=0
background_speed=0.5

pipe_image=pygame.image.load("assets/sprites/pipe-green.png")
pipe_image=pygame.transform.scale(pipe_image,(60,320))
pipe_image_flipped = pygame.transform.flip(
    pipe_image, False, True
)

pipe_x=300
pipe_gap=170
pipe_speed=0.25

pipe_top_y = -100
pipe_bottom_y = pipe_top_y + 320 + pipe_gap

#sound
pygame.mixer.init()

#jump sound
jump_sound=pygame.mixer.Sound("assets/audio/wing.wav")
jump_sound.set_volume(0.5)

#hit sound
hit_sound=pygame.mixer.Sound("assets/audio/hit.wav")
hit_sound.set_volume(1)

def reset_pipes():
    global pipe_x,pipe_top_y,pipe_bottom_y
    
    pipe_x=400
    
    pipe_top_y=random.randint(-220,-80)
    pipe_bottom_y=pipe_top_y+320+pipe_gap
    

    
running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity=jump_strength
                jump_sound.play()
                
    bird_velocity += gravity
    bird_y += bird_velocity
    
    # if bird_y > 350:
    #     bird_y = 350
    #     bird_velocity = 0
        
    # move background    
    background_x-=background_speed
    
    
    # screen.blit(background, (0, 0)) # Draw the background onto the screen
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x+400, 0))
    
    
    # Reset background
    if(background_x<= -400):
        background_x=0
    
    pipe_x-=pipe_speed
    screen.blit(pipe_image_flipped,(pipe_x,pipe_top_y))    
    screen.blit(pipe_image,(pipe_x,pipe_bottom_y)) 
    
    #reset the pipes
    if(pipe_x<30):
        reset_pipes()
        
    screen.blit(bird,(bird_x,bird_y))
    
    #draw ground    
    screen.blit(ground,(ground_x,ground_y))
    
    #create collision rectangles
    bird_rect=pygame.Rect(bird_x,bird_y,40,30)
    
    top_pipe_rect=pygame.Rect(pipe_x,pipe_top_y,60,320)
    bottom_pipe_rect=pygame.Rect(pipe_x,pipe_bottom_y,60,320)
    
    ground_rect=pygame.Rect(ground_x,ground_y,400,100)
    
    #check collision with pipes or ground
    if(bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect) or bird_rect.colliderect(ground_rect)):
        hit_sound.play()
        pygame.time.wait(300) #allow the sound to play
        print("game over!")
        running=False
    pygame.display.flip()    
pygame.quit