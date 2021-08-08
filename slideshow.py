import pygame, os, sys, argparse, random

parser = argparse.ArgumentParser(description='Creates a slideshow')
parser.add_argument('path', help="the directory to get the images from")
args = parser.parse_args()

WIDTH = 1920
HEIGHT = 1080
window_size = (WIDTH, HEIGHT)
images = []
for dirname, _, filenames in os.walk(str(args.path)):
    for filename in filenames:
        #print(os.path.join(dirname, filename))
        if filename[-1] == 'g':
            print(filename)
            images.append(pygame.image.load(os.path.join(dirname, filename)))

#scale the images
for i in range(len(images)):
    img = images[i]
    width=WIDTH   #Window size a bit smaller than monoitor size
    height=width*img.get_height()/img.get_width()  # keep ratio

    if height > HEIGHT:  # too tall for screen
        width = width * (HEIGHT)/height  # reduce width to keep ratio 
        height = HEIGHT  # max height

    new_image_size = (int(width),int(height))#(images[i].get_rect().width, images[i].get_rect().height)
    images[i] = pygame.transform.smoothscale(images[i], new_image_size)


pygame.init()
pygame.mixer.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
screen = pygame.display.set_mode(window_size, pygame.NOFRAME)
pygame.display.set_caption("Slideshow")
clock = pygame.time.Clock()

current_image_index = random.randrange(0, len(images))

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                current_image_index = (current_image_index + 1) % len(images)
            if event.key == pygame.K_RIGHT:
                current_image_index = (current_image_index - 1) % len(images)



    screen.fill((0,0,0))

    screen.blit(images[current_image_index], (WIDTH/2-images[current_image_index].get_rect().width/2,HEIGHT/2-images[current_image_index].get_rect().height/2))

    pygame.display.flip()       

pygame.quit()