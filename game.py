import pygame
import pygame_widgets
from pygame_widgets.button import Button

def main():
    maxgift = 5
    current_gift = 0
    print('thank so..what do we do first? 1-lets go look in the house 2-go out and look in the yard ')
    a = int(input())
    if a == 1:
        print('in Ded Morozs room you find a note with a riddle:')
        print('Riddle:Im green, but not a Christmas tree,  I can be as soft as a pillow.  What is it?')
        riddle = input()
        if riddle == 'cone':
            print('youre right')
            current_gift+=1
            print( 'maybe we can try to look under the tree?1-yes 2-no')
            l = int(input())
            if l==1:
                print('oh you find some gifts!')
                current_gift+=1
                print('you take'+str(current_gift)+'gifts')
            else:
                print('you can look in the bedrom 1-yes 2-no')
                p = int(input())
                if p==1:
                    print('oh you find some gifts!')
                    current_gift+=1
                    print('you take'+str(current_gift)+'gifts')
                else:
                    print('you take'+str(current_gift)+'gifts')
        else:
            print('no its wrong, try again')
            riddle = input()
            if riddle == 'cone':
                current_gift+=1
                print('you take'+str(current_gift)+'gifts')
            else:
                print('no its wrong, but maybe we can try to look under the tree?1-yes 2-no')
                s = int(input())
                if s==1:
                    print('oh you find some gifts!')
                    current_gift+=1
                    print('you take'+str(current_gift)+'gifts')
                else:
                    print('you can look in the bedrom 1-yes 2-no')
                    d = int(input())
                    if d==1:
                        print('oh you find some gifts!')
                        current_gift+=1
                        print('you take'+str(current_gift)+'gifts')
                    else:
                        print('you take'+str(current_gift)+'gifts')
    if a == 2:
        print('under the tree you find a cone with a note:')
        print('Riddle:I am white and fluffy, my name start Snow.  But if you dazzle me, I would soon melt here')
        riddle = input()
        if riddle == 'snowman':
            print('youre right')
            current_gift+=1
            print( 'maybe we can try to go to the right side?1-yes 2-no')
            c = int(input())
            if c==1:
                print('oh you find some gifts!')
                current_gift+=1
                print('you take'+str(current_gift)+'gifts')
            else:
                print('maybe left side? 1-yes 2-no')
                b = int(input())
                if b==1:
                    print('oh you find some gifts!')
                    current_gift+=1
                    print('you take'+str(current_gift)+'gifts')
                else:
                    print('you take'+str(current_gift)+'gifts')
        else:
            print('no its wrong, try again')
            riddle = input()
            if riddle == 'snowman':
                current_gift+=1
                print('you take'+str(current_gift)+'gifts')
            else:
                print('no its wrong, but maybe we can try to go to the right side side?1-yes 2-no')
                n = int(input())
                if n==1:
                    print('oh you find some gifts!')
                    current_gift+=1
                    print('you take'+str(current_gift)+'gifts')
                else:
                    print('maybe left side? 1-yes 2-no')
                    x = int(input())
                    if x==1:
                        print('oh you find some gifts!')
                        current_gift+=1
                        print('you take'+str(current_gift)+'gifts')
                    else:
                        print('you take'+str(current_gift)+'gifts')

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('santa')
button = Button(
    # Mandatory Parameters
    screen,  # Surface to place button on
    100,  # X-coordinate of top left corner
    300,  # Y-coordinate of top left corner
    250,  # Width
    100,  # Height

    # Optional Parameters
    text='help to find gifts',  # Text to display
    fontSize=35,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(255, 255, 255),  # Colour of button when not being interacted with
    hoverColour=(150, 0, 0),  # Colour of button when being hovered over
    pressedColour=(0, 200, 20),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: print('okay')  # Function to call when clicked on
)
running = True
while running:
    events = pygame.event.get()
    for event in events :
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    background = pygame.image.load('i.png')
    sprite = pygame.image.load('g.jpg')
    sp = pygame.transform.scale(sprite,(200,150))
    screen.blit(background, (0, 0))
    screen.blit(sp, (500, 450))
    
    

    def render_text(text, font_size, color=(255, 255, 255)):
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()
    welcome_text, welcome_rect = render_text('oh no! someone stole all the gifts from Ded Moroz ..dear friend, help us to find them', 25)
    welcome_rect.center = (400, 150)
    screen.blit(welcome_text, welcome_rect)
    
    pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
    pygame.display.update()
    
pygame.quit()

main() 
 





