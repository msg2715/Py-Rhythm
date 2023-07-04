import pygame

# 초기화
pygame.init()

# 창 이름 설정
pygame.display.set_caption("main")

# 화면크기 설정
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN) # 화면크기 - 풀스크린


# fps
fpsclock = pygame.time.Clock()



# 메인화면
running = True
def main():
    game_paused = False
    
    while True:
        
        # 자투리 설정
        fpsclock.tick(60) # fps 설정
        font = pygame.font.SysFont('malgungothicsemilight', 80)
        
        
        # 배경화면
        screen.blit(pygame.image.load("img\main_BG.png"), (0, 0))
        
        
        # START 버튼
        text_start = font.render('START', True, (255, 255, 255))
        text_start_size = text_start.get_rect().size # START 텍스트의 rect의 size 가져오기
        text_start_width = text_start_size[0] # 가로 사이즈
        text_start_height = text_start_size[1] # 세로 사이즈
        screen.blit(text_start, (960 - (text_start_width / 2), 500))
        
        
        # 이벤트 루프
        for event in pygame.event.get():
            pass
        
        
        # 화면 출력
        pygame.display.update()
        

def option(): # 옵션화면
    while True:
        fpsclock.tick(60) # fps 설정 - 60
        
        # 스프라이트 설정
        screen.blit(pygame.image.load("img\option_BG.png"), (0, 0)) # 배경화면 출력
        
        
    
        # 화면 출력
        pygame.display.update()

main()