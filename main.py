import pygame, sys, random

pygame.font.init()

WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

WHITE = (200, 200, 200)
BLUE = (40, 100, 200)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

FONT = pygame.font.SysFont('comicsans', 50)

FPS = 60

def main():
    ball = Ball()
    paddle = Paddle()
    
    score = 0
    health = 10
    tick_count = 0
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            
        tick_count += 1
        
        paddle_width, x_dif, acc, speed = difficulty_level(score)
        
        if pygame.Rect.colliderect(paddle.col_rect, ball.rect) == True and tick_count > 0:
            ball.bounce(x_dif, acc, speed)
            tick_count = -4
            score += 1
        elif ball.rect.y >= HEIGHT+100:
            ball.rect.x, ball.rect.y = WIDTH/2, 0
            tick_count = 0
            health -= 1
            ball.remove()
            ball = Ball()


        paddle.update(paddle_width)
        ball.move(tick_count)
        draw_window(ball, paddle, health, score)
    pygame.quit()
    
def draw_window(ball, paddle, health, score):
    WIN.fill(WHITE)
    health_text = FONT.render("Health: " + str(health), 1, BLACK)
    score_text = FONT.render("Score: " + str(score), 1, BLACK)
    WIN.blit(health_text, (WIDTH/2-300, 100))
    WIN.blit(score_text, (WIDTH/2+100, 100))
    pygame.draw.rect(WIN, BLACK, paddle.rect)
    pygame.draw.rect(WIN, RED, ball.rect)
    pygame.display.update()
    
def difficulty_level(score):
    if score > 300:
        return [100, 8, (12, 16), (18, 27)]
    if score > 260:
        return [120, 7, (13, 15), (18, 26)]
    if score > 220:
        return [120, 6, (12, 14), (18, 25)]
    if score > 180:
        return [140, 5, (10, 12), (18, 24)]
    if score > 150:
        return [140, 8, (12, 16), (18, 27)]
    if score > 130:
        return [140, 7, (13, 15), (18, 26)]
    if score > 100:
        return [140, 6, (12, 14), (18, 25)]
    if score > 80:
        return [160, 5, (10, 12), (18, 24)]
    if score > 60:
        return [160, 4, (10, 10), (18, 23)]
    if score > 30:
        return [180, 3, (8, 9), (18, 22)]
    else:
        return [200, 2, (6, 7), (17, 20)]
    
class Paddle():
    def __init__(self):
        self.rect = pygame.Rect(WIDTH/2-100, HEIGHT-100, 200, 30)
        self.col_rect = pygame.Rect(WIDTH/2-100, HEIGHT-120, 200, 80)
        
        
    def update(self, paddle_width):
        self.col_rect.x, self.col_rect.y = self.rect.x, self.rect.y-20
        self.rect.centerx = (WIDTH/2)+(pygame.mouse.get_pos()[0]-WIDTH/2)*6
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= WIDTH-self.rect.width:
            self.rect.x = WIDTH-self.rect.width
        self.col_rect.width = paddle_width
        self.rect.width = paddle_width


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()    
        self.rect = pygame.Rect(WIDTH/2, 0, 10, 10)
        self.vel_x = random.randint(-2, 2)
        self.vel_y = 0
        self.acc = 0.008
        self.speed = -20
        
    def bounce(self, x_dif, acc, speed):
        self.acc = random.randint(acc[0], acc[1])/100
        self.speed =  -random.randint(speed[0], speed[1])
        self.vel_y = self.speed
        self.vel_x = random.randint(-x_dif, x_dif)*x_dif/3
        

    def move(self, tick_count):
        self.vel_y = self.vel_y + self.acc*tick_count
        
        if self.rect.x >= WIDTH-10 or self.rect.x <= 10:
            self.vel_x = -self.vel_x

        self.rect.y += self.vel_y
        self.rect.x += self.vel_x

        

    
    
if __name__ == "__main__":
    main()