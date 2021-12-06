from operator import mul
import pygame
import numpy as np
import keras

multiple = 20

width = 28*multiple
height = 28*30

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Magic number guesser")
clock = pygame.time.Clock()

model = keras.models.load_model('model.h5')

loop = True
color = "white"
cnt = 0

screen.fill((255,255,255))
pygame.draw.rect(screen, 0, ((width/2)-280,0,28*20,28*20))

# defining a font
smallfont = pygame.font.SysFont('Corbel',200)
  
# rendering a text written in
# this font
# pygame.draw.rect(screen,0,[100,height - 100,100,50])

while loop:
    try:
        # pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pygame.draw.rect(screen, 0, ((width/2)-280,0,28*20,28*20))
                    pygame.draw.rect(screen, color, (0,28*20,width,height))

                if event.key == pygame.K_s:
                    pygame.draw.rect(screen, color, (0,28*20,width,height))

                    img = (np.array(pygame.surfarray.array2d(screen))[:28,:28]).T
                    img[img == -1] = 1

                    img = np.resize(img,(28,28,1))
                    img = np.array([img])

                    pred = model.predict(img)

                    text = smallfont.render(['0','1','2','3','4','5','6','7','8','9'][np.argmax(pred[0])] , True , (0,0,0))
                    screen.blit(text , (width/2-40,height - 200))
                    


    
        px, py = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1,0,0) and py < 560:
            pygame.draw.rect(screen, (255,255,255), (px,py,multiple*2,multiple*2))
            pygame.draw.rect(screen, (255,255,255), (px/multiple,py/multiple,2,2))

        if event.type == pygame.MOUSEBUTTONUP:

            pygame.draw.rect(screen, color, (0,28*20,width,height))

            img = (np.array(pygame.surfarray.array2d(screen))[:28,:28]).T
            img[img == -1] = 1

            img = np.resize(img,(28,28,1))
            img = np.array([img])

            pred = model.predict(img)

            text = smallfont.render(['0','1','2','3','4','5','6','7','8','9'][np.argmax(pred[0])] , True , (0,0,0))
            screen.blit(text , (width/2-40,height - 200))
            
        pygame.display.update()
        clock.tick(1000)
    except Exception as e:
        # print(e)
        pygame.quit()
        
pygame.quit()